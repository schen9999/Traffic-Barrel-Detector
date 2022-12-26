import cv2

img = cv2.VideoCapture('C:/Users/Scott Chen/OneDrive/Desktop/FIRE Photos/Vid.mp4')

while (True):

    ret, frame = img.read()

    if not ret:
        break
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('gray image', grayFrame)
    cv2.imshow('video original', frame)

    if cv2.waitKey(1) == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()

