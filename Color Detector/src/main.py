import config
import cv2 as cv
import utils

def main():
    kernel = cv.getStructuringElement(cv.MORPH_RECT, config.MORPH_KERNEL_SIZE) 

    video_capture = cv.VideoCapture(0) 

    try:
        if not video_capture.isOpened():
            print("Could not open video capture.")
            return

        # === Configure Camera Resolution ===
        video_capture.set(cv.CAP_PROP_FRAME_WIDTH, config.TARGET_WIDTH)
        video_capture.set(cv.CAP_PROP_FRAME_HEIGHT, config.TARGET_HEIGHT)

        # === User Selects Color ===
        current_color = utils.select_initial_color(config.VALID_COLORS)
        color_limits = utils.track_color(current_color)
        
        # === Quick Hardware Warmup ===
        for _ in range(config.WARMUP_FRAMES): # Grab & discard 5-10 frames so auto-exposure/white-balance stabilize
            video_capture.read()

        print("Tracking started. Press '1'-'6' to change colors, or 'q' to quit.")

        # === Main Video Loop ===
        while True:
            success, frame = video_capture.read()

            if not success:
                print("End of video stream.")
                break

            key_press = cv.waitKey(1) & 0xFF
    
            # === Check for Quit Command 'Q' ===
            if key_press == ord('q'):
                break

            # === Check for Color Change Command (keys '1' through '6') ===
            if key_press in config.COLOR_KEY_MAP:
                new_color = config.COLOR_KEY_MAP[key_press]

                if new_color != current_color:
                    current_color = new_color
                    color_limits = utils.track_color(current_color)

            # === Frame Processing ===
            frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) 
            color_mask = utils.build_combined_mask(frame_hsv, color_limits) 
            clean_mask = cv.morphologyEx(color_mask, cv.MORPH_OPEN, kernel, iterations=2) # Noise Reduction (Morphological Opening)

            # === Track Contours ===
            contours, _ = cv.findContours(clean_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

            if contours:
                largest_contour = max(contours, key=cv.contourArea)

                if cv.contourArea(largest_contour) > config.MIN_CONTOUR_AREA:
                    x, y, w, h = cv.boundingRect(largest_contour)
                    cv.rectangle(frame, (x, y), (x + w, y + h), config.BOX_COLOR, config.BOX_THICKNESS)

            # === Display Tracking Color ===
            color_label = f"Tracking {current_color.upper()}"
            cv.putText(frame, color_label, (10, 30), config.TEXT_FONT, config.TEXT_SCALE, config.TEXT_COLOR_OUTLINE, config.TEXT_THICKNESS_OUTLINE)
            cv.putText(frame, color_label, (10, 30), config.TEXT_FONT, config.TEXT_SCALE, config.TEXT_COLOR_FILL, config.TEXT_THICKNESS_FILL)

            # === Display Videos ===
            cv.imshow("Webcam Stream", frame)
            cv.imshow("Color Mask", clean_mask)
    finally:
        # === Cleanup ===
        video_capture.release()
        cv.destroyAllWindows()

if __name__ == "__main__":
    main()