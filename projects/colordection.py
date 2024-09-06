import cv2 as cv
import numpy as np

# Une fonction pour crEer la fEnetre avec les TrackBars deCu 
def create_trackbars():
    cv.namedWindow("TrackBars")
    cv.resizeWindow("TrackBars", 640, 240)
    cv.createTrackbar("Hue Min", "TrackBars", 0, 179, lambda e: ...)
    cv.createTrackbar("Hue Max", "TrackBars", 179, 179, lambda e: ...)
    cv.createTrackbar("Sat Min", "TrackBars", 0, 255, lambda e: ...)
    cv.createTrackbar("Sat Max", "TrackBars", 255, 255, lambda e: ...)
    cv.createTrackbar("Val Min", "TrackBars", 0, 255, lambda e: ...)
    cv.createTrackbar("Val Max", "TrackBars", 255, 255, lambda e: ...)


create_trackbars()

cap = cv.VideoCapture(0)
img = cv.imread("assets/ton_image.jpg")

while True:

    img = cv.resize(img, (640, 450))
    # Etape1: bgr2hsv image
    seed_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Assigner les valeurs des TrackBars aux variables
    hmin = cv.getTrackbarPos("Hue Min", "TrackBars")
    hmax = cv.getTrackbarPos("Hue Max", "TrackBars")
    smin = cv.getTrackbarPos("Sat Min", "TrackBars")
    smax = cv.getTrackbarPos("Sat Max", "TrackBars")
    vmin = cv.getTrackbarPos("Val Min", "TrackBars")
    vmax = cv.getTrackbarPos("Val Max", "TrackBars")

    lower = np.array([hmin, smin, vmin])
    upper = np.array([hmax, smax, vmax])

    mask = cv.inRange(seed_img, lower, upper)
  
    # Appliquer le mask sur l'image
    result = cv.bitwise_and(img, img, mask=mask)

    cv.imshow("Original Image", img)
    cv.imshow("mask", mask)
    cv.imshow("Result", result)
    cv.imshow("HSV image", seed_img)
  
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
