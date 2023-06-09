import cv2


def make_sketch(img):
    grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(grayed)
    blurred = cv2.GaussianBlur(inverted, (19,19), sigmaX=0, sigmaY=0)
    result = cv2.divide(grayed, 255 - blurred, scale=256)
    return result
