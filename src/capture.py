import numpy as np
from PIL import ImageGrab
import cv2

class ScreenCapture:
    def __init__(self, x1=0, y1=40, x2=800, y2=640):
        self.bbox = (x1, y1, x2, y2)
    
    def capture_screen(self):
        """Capture a portion of the screen and convert it to a numpy array."""
        screen = ImageGrab.grab(bbox=self.bbox)
        return cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2RGB)
    
    def start_capture_loop(self, process_frame=None):
        """Start a continuous capture loop with optional frame processing."""
        try:
            while True:
                frame = self.capture_screen()
                
                if process_frame:
                    frame = process_frame(frame)
                
                cv2.imshow('GTADriver', frame)
                
                # Press 'q' to quit
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
        finally:
            cv2.destroyAllWindows()
