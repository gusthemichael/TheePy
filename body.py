import cv2
from glob import glob

body_csc = cv2.CascadeClassifier('haarcascade_fullbody.xml')

#METRISEIS
im_count =  0 #gia na tsekaro poses eikones anoigo
ll = []#i lista me ta parathira poy epistrefei o al/mos

def haarCascade(imageFile):
     image = cv2.imread(imageFile)
     listOfRectangles = []
     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     body = body_csc.detectMultiScale(gray, 1.3, 1)
     
    
     for (x,y,w,h) in body:
         
         
         print("I DID IT")
         listOfRectangles.append(imageFile)
         listOfRectangles.append(x)
         listOfRectangles.append(y)
         listOfRectangles.append(w)
         listOfRectangles.append(h)
         cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
         cv2.imshow('goat',image)
         cv2.waitKey(0)
         
     return listOfRectangles
        




#find the body Haar Cascade
for imageF in glob('*.png'):
     im_count += 1
         
     ret = haarCascade(imageF)
     ll.append(ret)
     
    
        

#emfanisi eikonas


cv2.destroyAllWindows()





print('The number of images is', im_count)
print('The number of rectangle is', ll)





