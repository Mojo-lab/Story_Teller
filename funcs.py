#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 21:15:34 2021

@author: govardhan
working with opencv , pytessaract and pyttsx3 
"""
'''install package
pip install pytesseract
pip install pyttsx3
'''
#import necessary packages
import pytesseract
import cv2
from gtts import gTTS
import os
app_path = os.path.dirname(os.path.realpath('__file__'))
p = '/'

def Text_to_speech(Message,timestamp):
    speech = gTTS(text = Message)
    speech.save(app_path+p+'static'+p+'audio'+p+timestamp+'_DataFlair.mp3')
    path = timestamp+'_DataFlair.mp3'
    return path
    

def scan_image(img_loc):
    """
    

    Parameters
    ----------
    img_loc : str
        enter the loaction of the image and the image name with its format

    Returns
    -------
    the scanned text is being returned

    """
    img = cv2.imread(img_loc,0)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    hImg,wImg,_ = img.shape
    boxes = pytesseract.image_to_data(img)
    text = ''
    for x,b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            if len(b) == 12:
                text = text+' '+b[11]
                print(text)
    text = text+' .'+' End of reading.'
    return text













