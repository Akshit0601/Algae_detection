import sys
import numpy as np
import cv2
np.set_printoptions(threshold=sys.maxsize)
img=cv2.imread("algae.png")

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

#print(interior_points,np.ndim(interior_points))     
length=len(interior_points)

#np.append(arr, values)
for i in range(length-1):
    
    y,x=interior_points[i]
    y1,x1=interior_points[i+1]
  #  if(y!=(y+1) or x!=(x+1)):
        
    
    
    
c1=interior_points[0]
c1=c1[::-1]

c2=interior_points[length-1]
c2=c2[::-1]



color=[0,0,255]
detected_green=cv2.rectangle(img,c1,c2,color,2)


cv2.imshow("original image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


    
