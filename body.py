import cv2
from glob import glob

body_csc = cv2.CascadeClassifier('haarcascade_fullbody.xml')

#METRISEIS
im_count =  0 #gia na tsekaro poses eikones anoigo
#rectList = []#i lista me ta parathira poy epistrefei o al/mos

def haarCascade(imageFile):
     image = cv2.imread(imageFile)
     detectRecCoordinates = []
     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     body = body_csc.detectMultiScale(gray, 1.3, 1)
     
    
     for (x,y,w,h) in body:
         
         
         #print("I DID IT")
         #detectRecCoordinates.append(imageFile)
         detectRecCoordinates.append(x)
         detectRecCoordinates.append(y)
         detectRecCoordinates.append(w)
         detectRecCoordinates.append(h)
         cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
         cv2.imshow('goat',image)
         cv2.waitKey(0)
         
     return detectRecCoordinates
        

def getGtbb(imageFile):
    nameOfFile = imageFile
    textFile = open("annot.txt", "r")
    for line in textFile:
        if nameOfFile in line: 
            coord = []
            step_0 = line.strip()
            step = step_0.split(' ')
            for i in range(2, len(step)): 
                coord.append(int(step[i]))
    return coord

def checkIntersection(x,y,w,h,x1,y1,w1,h1):
    print("The real are: ", x,y,w,h)
    print("The test are: ", x1,y1,w1,h1)
    if x1+w1<x or x1>x+w or y1+h1<y or y1>y+h or x1+w1<x+w/2 or x1>x+w/2 or y1+h1<y+h/2 or y1>y+h/2:
        return True


#find the body Haar Cascade
for imageF in glob('*.png'):
     im_count += 1
     rectList = haarCascade(imageF)
     realCoord = getGtbb(imageF)
    # print('The number of rectangle is', rectList)
    # print(type(rectList))
    # print('Real coord are', realCoord)
    # print(type(realCoord))
     xreal = realCoord[0]
     yreal = realCoord[1]
     wreal = realCoord[2]
     hreal = realCoord[3]
    
     for j in range(0, len(rectList),  4):
         xtest = rectList[j]
         ytest = rectList[j+1]
         wtest = rectList[j+2]
         htest = rectList[j+3]
         if checkIntersection(xreal,yreal,wreal,hreal,xtest,ytest,wtest,htest):
             print("MISS")
         else:
             print("HIT")

    


#emfanisi eikonas


cv2.destroyAllWindows()

'''
print('The number of images is', im_count)
print('The number of rectangle is', rectList)
print('Real coord are', realCoord)





'''
