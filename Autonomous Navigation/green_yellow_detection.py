#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 19:38:01 2022

@author: akshitshishodia
"""
#import sys
import numpy as np
import cv2
#import imutils
from image_slicer import slice
from math import dist
#import os
import time
#from gpiozero import LED

#led_left=LED(17)
#led_right=LED(18)

#np.set_printoptions(threshold=sys.maxsize)
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

def navigation(v1,v2):
    l=[v1[0],v2[1]]
    return dist(list(v1),l)*dist(list(v2),l)

def fun1(mask):
    dup_img=np.zeros(np.shape(img),dtype=np.uint8)
    for idx,i in np.ndenumerate(mask):
        if(i==255):
            dup_img[idx]=(0,255,0)
    return dup_img

area_left,area_right=0,0

vid=cv2.VideoCapture(0)

#vid.set(cv2.CAP_PROP_BUFFERSIZE,2)


while(True):
   # if(not vid.grab()):
    #    break
    
    print(time.time())
    
    ret,frame=vid.read()
    frame=cv2.resize(frame,(300,int(frame.shape[0]*(300/frame.shape[1]))),interpolation=cv2.INTER_AREA)
    
    cv2.imwrite("temp.png",frame)
    T_class=slice("temp.png",4,save=True)
    slice_part=list()

    for j in range (4):
        
        img=cv2.imread(T_class[j].basename+".png")
        #print(img.shape)
        
        cvt_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        lower=np.array([30,100,100])
        upper=np.array([60,255,255])
        mask=cv2.inRange(cvt_img,lower,upper)
        dup_img=fun1(mask)
        cvt_dupimg=cv2.cvtColor(dup_img,cv2.COLOR_BGR2GRAY)

        
        edged1=cv2.Canny(dup_img,30,200)
        c,hierarachy=cv2.findContours(edged1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        #print(len(c))
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
            if(j==0 or j==2):
                area_left=navigation(corner, opp_corn)+area_left
            elif(j==1 or j==3):
                area_right=area_right+navigation(corner,opp_corn)
                
                
            # cv2.imshow("original",img)
            # cv2.waitKey(0)
            
            cv2.rectangle(img,corner,opp_corn,[0,0,255],1)
        
        
        slice_part.append(img)
        
           
        #print(left,right,top,bottom)
    im_f=cv2.vconcat([cv2.hconcat([slice_part[0],slice_part[1]]),cv2.hconcat([slice_part[2],slice_part[3]])])
    im_f=cv2.resize(im_f,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
   # print(area_left)
   # print(area_right)
    
    if(area_left>area_right):
      
        print("go left")
       # led_right.off()
        #led_left.on()
    elif(area_left<area_right):
        print("go right")
    
    else:
        print("go straight")
        
       # led_left.off()
       # led_right.on()
    
    cv2.imshow("detected",im_f)
    print(time.time())
    #for k in range(4):
       # os.remove(T_class[i].basename+".png")
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
