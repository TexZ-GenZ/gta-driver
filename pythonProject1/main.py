import numpy as np
from PIL import ImageGrab
import cv2
import time

last_time = time.time()

while(True):
    printscreen_pil = ImageGrab.grab(bbox =(0,40,800,640))
    # printscreen_numpy = np.array(printscreen_pil.getdata(),dtype='uint8')

    # .reshape(printscreen_pil.size[1], printscreen_pil.size[0], 3)

    print('Loop took {} seconds'.format(time.time() - last_time))
    last_time = time.time()
    cv2.imshow('window',cv2.cvtColor(np.array(printscreen_pil)))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break