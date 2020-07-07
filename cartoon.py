# importing openCV 
import cv2 
 
# reading image
img_file = input("Enter image filename here: ")    # make sure image is located in the same folder/directory where code file is stored
img = cv2.imread(img_file) 
   
# Edges 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
gray = cv2.medianBlur(gray, 1)
edges = cv2.adaptiveThreshold(gray, 500, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
   
# Cartoonization 
color = cv2.bilateralFilter(img, 7, 3000, 3000)
cartoon = cv2.bitwise_and(color, color, mask=edges) 
   
   
cv2.imshow("Image", img) 
cv2.waitKey(0) 
cv2.imshow("Edges", edges)
cv2.waitKey(0)  
cv2.imshow("Cartoon", cartoon) 
cv2.waitKey(0) 
cv2.destroyAllWindows()