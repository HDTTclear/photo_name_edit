# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 21:39:22 2019

@author: 16000
"""
from PIL import Image
import re
import os
import numpy as np
import xlrd
import glob
def convertjpg(jpgfile,outdir,width=600,height=800):
    img=Image.open(jpgfile)
    try:
        new_img=img.resize((width,height))   
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)
        
for jpgfile in glob.glob(r"C:\Users\16000\Desktop\result\*.jpg"):
    convertjpg(jpgfile,r"C:\Users\16000\Desktop\result");
