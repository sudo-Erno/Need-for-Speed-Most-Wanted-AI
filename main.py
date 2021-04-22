import pyautogui, time, os
import cv2
import numpy as np
from screen_capture import ScreenCapture

class AutoNFS():
    def __init__(self):
        pyautogui.FAILSAFE = True
        self.WIDTH = 1300
        self.HEIGHT = 750
        self.window = ScreenCapture(self.WIDTH, self.HEIGHT)

    def process_frame(self):

        while True:
            screenshot = self.window.capture()
            # screenshot = np.array(screenshot)
            
            minimap = screenshot[525:self.HEIGHT, 0:240]
        
            minimap_grayscale = cv2.cvtColor(minimap, cv2.COLOR_RGB2GRAY)
            minimap_hsv = cv2.cvtColor(minimap, cv2.COLOR_BGR2RGB)
            
            # Detect green
            green_lower = np.array([25, 52, 72], np.uint8)
            green_upper = np.array([102, 255, 255], np.uint8)
            green_mask = cv2.inRange(minimap_hsv, green_lower, green_upper)
            kernel = np.ones((5, 5))
            green_mask = cv2.dilate(green_mask, kernel)
            res_green = cv2.bitwise_and(minimap_hsv, minimap_hsv, mask = green_mask)

            # TODO Buscar una manera de alinear la linea para llegar al destino
            
            # matches = np.argwhere(green_mask==255)
            # mean_y = np.mean(matches[:,0])
            # # target = green_mask.shape[1] / 2
            # print(green_mask.shape)
            
            # th_v, img_ = cv2.threshold(minimap_grayscale, 105, 255, cv2.THRESH_BINARY)

            # cv2.imshow("Need for Speed", screenshot)
            cv2.imshow("Masked Image", res_green)

            if cv2.waitKey(1) == ord("q"):
                cv2.destroyAllWindows()
                break
    
    def forward(self):        
        # print("Go!")
        # pyautogui.keyDown("a")
        # time.sleep(2)
        # pyautogui.keyUp("a")
        # print("Done")
        pass

if __name__ == "__main__":
    agent = AutoNFS()
    agent.process_frame()
    # agent.forward()
