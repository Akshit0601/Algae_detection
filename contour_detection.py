"""
Created on Tue Aug 30 19:38:01 2022

@author: akshitshishodia
"""
import sys
import numpy as np
import cv2
np.set_printoptions(threshold=sys.maxsize)

#img=cv2.imread("serpentine.jpeg")
#img=cv2.imread("/Users/akshitshishodia/Desktop/python/iitg_lake_nude2.png")
img=cv2.imread("/Users/akshitshishodia/Desktop/python/algae05.png")
dup_img=np.zeros(np.shape(img),dtype=np.uint8)


cvt_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower=np.array([0,100,100])
upper=np.array([60,255,255])

mask=cv2.inRange(cvt_img,lower,upper)
interior_points=list()
for idx,i in np.ndenumerate(mask):
    if(i==255):
        interior_points.append(tuple(idx))
        dup_img[idx]=(0,255,0)
    x,y=idx
    
    
cv2.imshow("nla",dup_img)
cv2.waitKey(0)    
cv2.imshow("multiple_algae.png",cvt_img)
cv2.waitKey(0) 
cvt_dupimg=cv2.cvtColor(dup_img,cv2.COLOR_BGR2GRAY)

edged1=cv2.Canny(dup_img,30,200)
cnt,hierarchy=cv2.findContours(edged1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow("detection",img)
cv2.waitKey(0)
cv2.drawContours(img,cnt,-1,(0,0,255),1)      

cv2.imshow("detection",img)
cv2.waitKey(0)       
cv2.destroyAllWindows()
