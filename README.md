# Color Detector

A real-time color detection and tracking application using OpenCV. Select a color, and the app tracks it in your webcam feed.

## Features

- 🎨 Real-time color detection from webcam
- 🔄 Switch between 6 colors (red, orange, yellow, green, blue, purple)
- 📹 Adjustable video resolution and tracking parameters
- 🔊 Audio feedback using text-to-speech
- ⚡ Optimized with morphological operations for clean detection

## How It Works

1. Captures video from your webcam
2. Converts frames to HSV color space (more reliable than RGB)
3. Creates a binary mask for the selected color
4. Applies morphological operations to clean up noise
5. Detects contours and draws bounding box around tracked color
6. Speaks the color name via text-to-speech

## Requirements

- Python 3.8+
- Webcam/video input device
- Windows/Mac/Linux

## Installation

1. Clone or download this repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # source .venv/bin/activate  # On Mac/Linux
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

**Color not tracking well?**
- Adjust lighting in your environment
- Modify HSV ranges in `src/config.py`
- Ensure your object has solid color

**Webcam not opening?**
- Check if another app is using the camera
- Try a different video input device number in `main.py`

**Poor performance?**
- Lower `TARGET_WIDTH` and `TARGET_HEIGHT`
- Increase `MIN_CONTOUR_AREA` to filter more noise

## License

MIT License - Feel free to use this project