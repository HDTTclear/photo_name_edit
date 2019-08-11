# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 18:42:58 2019

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
        new_img=img.resize((width,height),Image.BILINEAR)   
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)


data_goto=xlrd.open_workbook(r'C:\Users\16000\Desktop\photo\详细信息.xlsx');table=data_goto.sheets()[0];
start=0;end=151;rows=end-start;name_list_goto=[];
for x in range(start,end):
    row =table.row_values(x);
    name_list_goto.append(row[2]);

data = xlrd.open_workbook(r'C:\Users\16000\Desktop\name_list.xls');sheet1 = data.sheets()[0];    
start=0;end=375;rows=end-start;name_list=[];photo_list=[];
for x in range(start,end):
 row =sheet1.row_values(x);
 name_list.append(str(row[6]).split('-')[0]);photo_list.append(row[7].split('%')[4][2:]);

path_name=r'C:\Users\16000\Desktop\photo\photo_all';
target=r'C:\Users\16000\Desktop\result';
for name in name_list_goto:
 if name in name_list:
  index_name=name_list.index(name);photo=photo_list[index_name];
  origin_photo=os.path.join(path_name,photo);
  target_photo=os.path.join(target,sheet1.row_values(name_list.index(name))[6]+'.jpg');
  os.rename(origin_photo,target_photo);

    


