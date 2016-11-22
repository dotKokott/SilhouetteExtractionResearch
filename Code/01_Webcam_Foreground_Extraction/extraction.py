import cv2
import numpy as np

def render():
    cam = cv2.VideoCapture(0)
    fgbg = cv2.createBackgroundSubtractorMOG2()
    kernel = np.ones((5,5),np.uint8)
    kernel = kernel

    while True:
        ret_val, img = cam.read()

        img = cv2.flip(img, 1)

        fgmask = fgbg.apply(img)
        back = fgbg.getBackgroundImage()

        erosion = cv2.erode(fgmask, kernel)
        dilate = cv2.dilate(erosion, kernel)

        im2, contours, hierarchy = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(img, contours, -1, (0,0,255), 2)
        cv2.imshow('Contour applied', img)
        cv2.imshow('Foreground mask', fgmask)

        if cv2.waitKey(1) == 27:
            break  # esc to quit

    cv2.destroyAllWindows()

def main():
    render()

if __name__ == '__main__':
    main()
