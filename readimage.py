import cv2
from glob import glob

body_csc = cv2.CascadeClassifier('haarcascade_fullbody.xml')
numberOfpics = 0
numberOfrecs = 0

for imageF in glob('*.png'):
    numberOfpics+=1
    image = cv2.imread(imageF)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    body = body_csc.detectMultiScale(gray, 1.2, 1)
    for (x,y,w,h) in body:
        numberOfrecs+=1
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
    
    #res = cv2.resize(image,(int(image.shape[1]/2),int(image.shape[0]/2)))

    #cv2.imshow(imageF,res)
    cv2.imshow(imageF,image)
    k = cv2.waitKey(0)
    if k == 32:
        cv2.destroyAllWindows()

print("Total no. of images:", numberOfpics)
print("Total no. of rectangles:", numberOfrecs)


