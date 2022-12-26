
import cv2

img = cv2.imread('C:/Users/chen7/OneDrive/Desktop/FIRE Photos/Template.png', 0)

cv2.imshow('Template', img)
cv2.waitKey(0)

cv2.destroyAllWindows()