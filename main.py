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
            
            # minimap = screenshot[525:self.HEIGHT, 0:240]
            # h = 750 - 30 - 550 = 170
            minimap = screenshot[550:self.HEIGHT-30, 35:205] # 240
        
            minimap_grayscale = cv2.cvtColor(minimap, cv2.COLOR_RGB2GRAY)
            
            # Detect green
            green_lower = np.array([70, 149, 70], np.uint8)
            green_upper = np.array([180, 255, 180], np.uint8)
            green_mask = cv2.inRange(minimap, green_lower, green_upper)
            kernel = np.ones((5, 5))
            green_mask = cv2.dilate(green_mask, kernel)
            res_green = cv2.bitwise_and(minimap, minimap, mask = green_mask)

            cv2.imshow("Minimap", res_green)
            cv2.imshow("Full Minimap", minimap)
            
            # Converting res_green to GRAY
            # g = cv2.cvtColor(res_green, cv2.COLOR_BGR2GRAY)
            
            # g = cv2.bilateralFilter(g, 30, 100, 150) # Baja la performance
            # _, g = cv2.threshold(g, 125, 250, cv2.THRESH_BINARY)

            # cv2.imshow("Green", g)

            b, g_, r = cv2.split(minimap)
            
            g_ = cv2.bilateralFilter(g_, 50, 130, 70) # Baja la performance
            th_v, g_ = cv2.threshold(g_, 115, 255, cv2.THRESH_BINARY) # 150
            cv2.imshow("Green II", g_)
            
            index = np.argwhere(g_==255) # index of pixels where the value is 255
            mean_x = np.mean(index[:,1])
            mean_y = np.mean(index[:,0])
            
            # Check if the mean_x and mean_y is nan
            # TODO How the car will follow the path...

            print(mean_x, mean_y)
            # Sets the coordinates of the minimap
            minimap_x_middle = g_.shape[1] / 2 # g.shape[1] --> Width component. g.shape[1] / 2 --> Midle of the width
            minimap_y_middle = g_.shape[0] / 2


            # print(minimap_x_middle, minimap_y_middle, mean)

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
