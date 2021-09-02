import cv2 # imorted necessary Libraray

img = cv2.imread("lion.jpg") # Loding the required image
cv2.imshow("Lion",img) #Showing the image
cv2.waitKey(0)

gry_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Converting the image into gray
cv2.imshow("Different Loin",gry_img) # Showing the Gray image
cv2.waitKey(0)

inverted_img = 255 - gry_img # converting the gray image into inverted
cv2.imshow("Inverted", inverted_img)# Showing the inverted image
cv2.waitKey(0)

blur = cv2.GaussianBlur(inverted_img,(21,21),0) # converting the image into blur using Gaussian Function
inv_blur = 255 - blur
pen_sketch = cv2.divide(gry_img,inv_blur,scale=255.0) # At last making the pencil Sketch...
cv2.imshow("Pencil Sketch",pen_sketch)
cv2.waitKey(0)