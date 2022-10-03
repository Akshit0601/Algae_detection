"""
Created on Tue Aug 30 19:38:01 2022

@author: akshitshishodia
"""
import sys
import numpy as np
import cv2
#import imutils
import image_slicer


np.set_printoptions(threshold=sys.maxsize)
#img=cv2.imread("serpentine.jpeg")
#img=cv2.imread("/Users/akshitshishodia/Desktop/python/iitg_lake_nude2.png")

def extreme(c):
    left=tuple(c[c[:, :, 0].argmin()][0])
    top=tuple(c[c[:,:,1].argmin()][0])
    right=tuple(c[c[:,:,0].argmax()][0])
    bottom=tuple(c[c[:,:,1].argmax()][0])
    return (left,top,right,bottom)

def for_left(left_init):
    global left
    if(left_init[0]<left[0]):
        
        left=left_init
        
def for_right(right_init):
    global right
    if(right_init[0]>right[0]):
        
        right=right_init
    
        
def for_top(top_init):
    global top
    if(top_init[1]<top[1]):
        
        top=top_init
        
def for_bottom(bottom_init):
    global bottom
    if(bottom_init[1]>bottom[1]):
        
        bottom=bottom_init
        
T_class=image_slicer.slice("algae05.png",4,save=True)
slice_part=list()

for j in range (4):       
    img=cv2.imread(T_class[j].basename+".png")
    print(img.shape)
    dup_img=np.zeros(np.shape(img),dtype=np.uint8)
    cvt_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower=np.array([30,100,100])
    upper=np.array([60,255,255])
    mask=cv2.inRange(cvt_img,lower,upper)
    interior_points=list()
   
    for idx,i in np.ndenumerate(mask):
        if(i==255):
            interior_points.append(tuple(idx))
            dup_img[idx]=(0,255,0)
        x,y=idx
    

    cvt_dupimg=cv2.cvtColor(dup_img,cv2.COLOR_BGR2GRAY)
    
    edged1=cv2.Canny(dup_img,30,200)
    c,hierarachy=cv2.findContours(edged1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    print(len(c))
    if(len(c)!=0):
        left,right,top,bottom=extreme(c[0])
        for i in range(1,len(c)):
            
            left_init,top_init,right_init,bottom_init=extreme(c[i])
            #print(left_init,top_init,right_init,bottom_init)
            
            for_left(left_init)
            for_right(right_init)
            for_top(top_init)
            for_bottom(bottom_init)
        
        corner=(left[0],top[1])
        opp_corn=(right[0],bottom[1])
        # cv2.imshow("original",img)
        # cv2.waitKey(0)
        
        cv2.rectangle(img,corner,opp_corn,[0,0,255],2)
    
    
    slice_part.append(img)
       
    #print(left,right,top,bottom)    
    
        
        
        
im_h1=cv2.hconcat([slice_part[0],slice_part[1]])

im_h2=cv2.hconcat([slice_part[2],slice_part[3]])
im_f=cv2.vconcat([im_h1,im_h2])


cv2.imshow("detected",im_f)
cv2.waitKey(0)
cv2.destroyAllWindows()
