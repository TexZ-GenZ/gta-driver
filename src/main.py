import time
from capture import ScreenCapture
from processing import ImageProcessor

def main():
    # Initialize screen capture and image processor
    capture = ScreenCapture()
    processor = ImageProcessor()
    
    # Track frame processing time
    last_time = time.time()
    
    def process_frame(frame):
        nonlocal last_time
        # Process frame (detect lanes)
        processed_frame = processor.detect_lanes(frame)
        
        # Calculate and display FPS
        print(f'Frame processed in {time.time() - last_time:.3f} seconds')
        last_time = time.time()
        
        return processed_frame
    
    # Start capture loop with frame processing
    capture.start_capture_loop(process_frame)

if __name__ == "__main__":
    main()
