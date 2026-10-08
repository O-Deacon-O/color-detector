# === Video Stream & Resolution Settings ===
MIN_CONTOUR_AREA = 500  # Filters out tiny background noise/dots
TARGET_WIDTH = 640
TARGET_HEIGHT = 480
WARMUP_FRAMES = 5

# === Application Color Mappings ===
VALID_COLORS = ("red", "orange", "yellow", "green", "blue", "purple")

COLOR_KEY_MAP = {
    ord('1'): "red",
    ord('2'): "orange",
    ord('3'): "yellow",
    ord('4'): "green",
    ord('5'): "blue",
    ord('6'): "purple",
}

# === HSV Color Detection Tuning Parameters ===
# === Center Hues (0–179 in OpenCV HSV space) ===
HUE_MAP = {
    "red": (0, 179),  # Returns two pairs because its hue wraps around (0-10 and 170-179)
    "orange": 10,
    "yellow": 30,
    "green": 60,
    "blue": 110,
    "purple": 135,
}

# === Standard Saturation/Value Range (to detect bright, saturated colors) ===
HUE_TOLERANCE = 10
LOWER_SATURATION_VALUE = 50
UPPER_SATURATION_VALUE = 255

# === Morphological Kernel for Noise Reduction ===
MORPH_KERNEL_SIZE = (5, 5)

# === UI & Text Display Formatting ===
TEXT_SCALE = 0.8
TEXT_COLOR_FILL = (255, 255, 255)  # White
TEXT_COLOR_OUTLINE = (0, 0, 0)  # Black
TEXT_THICKNESS_FILL = 2
TEXT_THICKNESS_OUTLINE = 10

# === Bounding Box Properties ===
BOX_COLOR = (0, 255, 0)  # Green
BOX_THICKNESS = 2
