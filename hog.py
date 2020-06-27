import cv2
from glob import glob


descriptor = cv2.HOGDescriptor()
descriptor.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

thereIs= False
numberOfpics = 0
numberOfrecs = 0

for imageF in glob('*.png'):
    numberOfpics+=1
    image = cv2.imread(imageF)
    (body, _) = descriptor.detectMultiScale(image,scale = 1.0)
    
    for (x,y,w,h) in body:
        numberOfrecs+=1
        thereIs = True
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
    
    if thereIs:
	thereIs = False
    	cv2.imshow(imageF,image)
    	k = cv2.waitKey(0)
    	if k == 32:
        	cv2.destroyAllWindows()
    
print("Total no. of images:", numberOfpics)
print("Total no. of rectangles:", numberOfrecs)
