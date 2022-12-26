import cv2

image = cv2.imread("C:/Users/Scott Chen/OneDrive/Desktop/FIRE Photos/VidScreenshot.png")
template = cv2.imread("C:/Users/Scott Chen/OneDrive/Desktop/FIRE Photos/Template.png")
(w,h) = template.shape[:2]

gray_Img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_Template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(gray_Img, gray_Template,
	cv2.TM_CCOEFF_NORMED)
(min_Val, max_Val, min_Loc, max_Loc) = cv2.minMaxLoc(result)

(startX, startY) = max_Loc
endX = startX + template.shape[1]
endY = startY + template.shape[0]

cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 3)

cv2.imshow("Output", image)
cv2.waitKey(0)
