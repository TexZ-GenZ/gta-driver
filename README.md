# GTADriver - Computer Vision for GTA

An experimental computer vision project that captures and processes the GTA game screen in real-time using Python, OpenCV, and PIL.

## Features
- Real-time screen capture
- OpenCV-based image processing
- Performance monitoring (frame processing time)

## Requirements
- Python 3.x
- OpenCV (cv2)
- Pillow (PIL)
- NumPy

## Setup
1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install opencv-python pillow numpy
```

## Usage
1. Start GTA
2. Run the script:
```bash
python main.py
```
3. Press 'q' to quit the application

## Project Structure
```
GTADriver/
├── src/               # Source code
│   ├── main.py       # Main application
│   ├── capture.py    # Screen capture utilities
│   └── processing.py # Image processing functions
├── requirements.txt   # Project dependencies
└── README.md         # Project documentation
```

## License
MIT License

## Contributing
Feel free to open issues or submit pull requests.
