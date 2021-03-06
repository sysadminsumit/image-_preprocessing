# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 01:01:05 2018

@author: Sumit
"""

import cv2
import numpy as np
import detect_face_pipe as df
import glob
import os


global global_image

counter = 100
video_list_input = glob.glob('dem_vid.mp4')

path = "C:/Users/AMIT/Desktop/image-_preprocessing"


for i in video_list_input:
    print(i)

    
    vidcap = cv2.VideoCapture(i)
    success,image = vidcap.read()
    width,height=image.shape[:2]
    #global_image =np.zeros(height*width*3).reshape((1,height,width,3))
    global_image = []
    global_image.append(image)
    count = 110
    while success:
        
        #print(count)
        file_name = 'amit' + str(count) + '.jpg'
        if count%11==0:  
            width,height=image.shape[:2]
            image=np.rot90(image,1)
            width1,height1=image.shape[:2]
            if width == height1:
                print(image.shape)
                global_image.append(image)
            
            
          # cv2.imwrite(os.path.join(path, file_name),image) # save frame as JPEG file 
            
             
        success,image = vidcap.read()
        #print('Read a new frame: ', success)
        count = count+1
    global_image = np.asarray(global_image)
    print(global_image.shape[0])

    obj = df.Detect(global_image)
    print(obj.unique_vector.shape)
