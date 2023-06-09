import cv2 as cv

def image_capture(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_classifier = cv.CascadeClassifier(
        cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)
    face = face_classifier.detectMultiScale(
       gray, scaleFactor=1.1, minNeighbors=5, minSize=(40,40)
    )
    for (x, y, w, h) in face:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    return rgb_img
