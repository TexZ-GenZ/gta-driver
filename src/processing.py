import cv2
import numpy as np

class ImageProcessor:
    @staticmethod
    def to_grayscale(frame):
        """Convert frame to grayscale."""
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    @staticmethod
    def detect_edges(frame, threshold1=100, threshold2=200):
        """Detect edges using Canny edge detection."""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.Canny(gray, threshold1, threshold2)
    
    @staticmethod
    def detect_lanes(frame):
        """Basic lane detection using edge detection and Hough transform."""
        # Convert to grayscale and detect edges
        edges = ImageProcessor.detect_edges(frame)
        
        # Define region of interest (lower half of the screen)
        height = frame.shape[0]
        roi = edges[height//2:, :]
        
        # Detect lines using Hough transform
        lines = cv2.HoughLinesP(roi, 1, np.pi/180, 50, 
                               minLineLength=100, maxLineGap=50)
        
        # Draw detected lines
        result = frame.copy()
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                y1 += height//2  # Adjust y coordinates back to original frame
                y2 += height//2
                cv2.line(result, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        return result
