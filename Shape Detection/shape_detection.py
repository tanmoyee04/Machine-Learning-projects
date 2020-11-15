# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 15:29:31 2020

@author: Tanmoyee
"""

import cv2
def getContours(img):  #function to detect shapes
    contours , heirarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)  #extracting the contours from the image
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area >100:
            cv2.drawContours(imgContours,cnt,-1,(0,0,0),2) #to draw counters
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True) #approximates a contour shape to another shape with less number of vertices depending upon the specified precision 
            objectCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx) #It is a straight rectangle, it doesn't consider the rotation of the object. So area of the bounding rectangle won't be minimum.

            if objectCor == 3:
                objectType = "Triangle"

            elif objectCor == 4: #here we need to differentiate between square and rectangle
                assRatio = w/float(h)
                if assRatio >0.95 and assRatio<1.05: #It is a square if its width and height are same
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objectCor == 5:
                objectType = "Pentagon"
            elif objectCor == 6 :
                objectType = "Hexagon"
            elif objectCor > 6: #check if it is a circle or not
                objectType = "Circle"
            else:
                objectType = "None"

            cv2.rectangle(imgContours,(x,y),(x+w,y+h),(0,255,0),2) #to make a rectangle arround the shape and write the name of the shape
            cv2.putText(imgContours,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2)

path = r"C:\Users\Tanmoyee\shape_test.png"
img = cv2.imread(path) #reading the image
imgContours = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting image to gray scale
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1) #smoothening of image using a Gaussian kernel where we need to specify the width and height of the kernel which should be positive and odd. We also should specify the standard deviation in the X and Y directions, sigmaX and sigmaY respectively.
imgCanny = cv2.Canny(imgBlur,50,50) #to get strong edges in the image. 1st= input img, 2nd= minVal, 3rd= maxVal or aperture size.
getContours(imgCanny)

cv2.imshow("Shapes",img)
cv2.imshow("output",imgContours)

cv2.waitKey(0)
