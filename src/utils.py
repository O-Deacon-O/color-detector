import config
import cv2 as cv
import numpy as np
import pyttsx3
import threading

_tts_lock = threading.Lock()

def build_combined_mask(frame_hsv: np.ndarray, color_limits: list) -> np.ndarray:
    """Creates a unified binary mask across all HSV ranges for the target color."""
    combined_mask = None
    
    for lower, upper in color_limits:
        current_mask = cv.inRange(frame_hsv, lower, upper)
        combined_mask = current_mask if combined_mask is None else cv.bitwise_or(combined_mask, current_mask)

    return combined_mask

def select_initial_color(valid_colors: tuple) -> str:
    """Prompts user until a valid color is picked."""
    while True:
        user_input = input(f"Pick a color ({', '.join(valid_colors)}): ").strip().lower()

        if user_input in valid_colors:
            return user_input
        
        print("Invalid color. Please try again.")

def track_color(selected_color: str) -> list:
    """Announces and returns HSV limits for the chosen color."""
    print_and_speak(f"Tracking: {selected_color.upper()}")
        
    return _get_color_range(selected_color)
        
def _get_color_range(color_name: str) -> list:
    """Returns a list of (lower_limit, upper_limit) HSV tuples for the given color.""" 
    if color_name not in config.HUE_MAP:
        raise ValueError(f"Unknown color: {color_name}. Choose from: {', '.join(config.HUE_MAP.keys())}")

    # === Red is a Special Case (Hue wraps around 0/179) ===
    if color_name == "red":
        lower_limit_1 = np.array([0, config.LOWER_SATURATION_VALUE, config.LOWER_SATURATION_VALUE], dtype=np.uint8)
        upper_limit_1 = np.array([config.HUE_TOLERANCE, config.UPPER_SATURATION_VALUE, config.UPPER_SATURATION_VALUE], dtype=np.uint8)
        
        lower_limit_2 = np.array([179 - config.HUE_TOLERANCE, config.LOWER_SATURATION_VALUE, config.LOWER_SATURATION_VALUE], dtype=np.uint8)
        upper_limit_2 = np.array([179, config.UPPER_SATURATION_VALUE, config.UPPER_SATURATION_VALUE], dtype=np.uint8)
        
        return [(lower_limit_1, upper_limit_1), (lower_limit_2, upper_limit_2)]

    # === Standard Colors ===
    else:
        hue = config.HUE_MAP[color_name]

        lower_hue = max(0, hue - config.HUE_TOLERANCE)
        upper_hue = min(179, hue + config.HUE_TOLERANCE)

        lower_limit = np.array([lower_hue, config.LOWER_SATURATION_VALUE, config.LOWER_SATURATION_VALUE], dtype=np.uint8)
        upper_limit = np.array([upper_hue, config.UPPER_SATURATION_VALUE, config.UPPER_SATURATION_VALUE], dtype=np.uint8)
        
        return [(lower_limit, upper_limit)]

def print_and_speak(text: str):
    """Prints text to console and speaks it asynchronously."""
    print(text)
    _speak_text(text)

def _speak_text(text: str):
    """Run text-to-speech in a separate thread."""
    def run():
        with _tts_lock:
            try:
                engine = pyttsx3.init()
                engine.say(text)
                engine.runAndWait()
                engine.stop()
            except Exception as e:
                print(f"TTS Error: {e}")

    thread = threading.Thread(target=run, daemon=True)
    thread.start()