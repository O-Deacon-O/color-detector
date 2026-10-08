# Color Detector

A real-time color detection and tracking application using OpenCV. Select a color, and the app tracks it in your webcam feed.

## Features

- Switch between 6 colors (red, orange, yellow, green, blue, purple)
- Audio feedback using text-to-speech

## How It Works

1. Captures video from your webcam
2. Converts frames to HSV color space (more reliable than RGB)
3. Creates a binary mask for the selected color
4. Applies morphological operations to clean up noise
5. Detects contours and draws bounding box around tracked color

## Requirements

- Python 3.8+
- Webcam/video input device
- Windows, macOS, or Linux

## Installation

1. Clone or download this repository.
2. Create and activate a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
# source .venv/bin/activate  # On macOS/Linux
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python src/main.py
```

**Controls:**
- `1-6` - Switch between colors (red, orange, yellow, green, blue, purple)
- `q` - Quit the application

**On startup:**
- You'll be prompted to pick a starting color
- The app will warm up your camera (5 frames)
- Point your webcam at the colored object you want to track

## Configuration

Edit `src/config.py` to customize:
- **Video resolution**: `TARGET_WIDTH`, `TARGET_HEIGHT`
- **Color detection ranges**: `HUE_MAP` (HSV values)
- **Contour filtering**: `MIN_CONTOUR_AREA`
- **Camera warmup**: `WARMUP_FRAMES`

## Troubleshooting

**Webcam not opening?**
- Check if another app is using the camera
- Try a different video input device number in `main.py`

**Color not tracking well?**
- Adjust lighting in your environment (Works best in neutral light)
- Modify HSV ranges in `src/config.py`
- Ensure your object has solid color

**Poor performance?**
- Lower `TARGET_WIDTH` and `TARGET_HEIGHT`
- Increase `MIN_CONTOUR_AREA` to filter more noise

## License

MIT License - Feel free to use this project
