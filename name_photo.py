# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 00:55:13 2019

@author: 16000
"""
import re

def atoi(text):
    return int(text) if text.isdigit() else text
#根据字符串中的自然数排序
def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]


#处理excel表格
import os
import numpy as np
import xlrd
#选择路径
data = xlrd.open_workbook('D:\pro\people.xlsx');
table = data.sheets()[0];


print(table)
start=1  #开始的行
end=8 #结束的行
rows=end-start
name_list=[]

for x in range(start,end):
    row =table.row_values(x)
    #print(row[0]);
    print(row[0].split('-',1)[0])
    name_list.append(row[0].split('-', 1)[0])

print(name_list);


#给图片命名
#选择路径
path_name='D:\pro\pic'
#path_name :表示你需要批量改的文件夹
i=0

file_list=os.listdir(path_name);
print(file_list);
#按自然数排序
file_list.sort(key=natural_keys);
print(file_list)

#for item in os.listdir(path_name):#进入到文件夹内，对每个文件进行循环遍历

    #os.rename(os.path.join(path_name,item),os.path.join(path_name,(str(i)+'.jpg')))#os.path.join(path_name,item)表示找到每个文件的绝对路径并进行拼接操作
    #i+=1
    
    
j=0
for item in file_list:#进入到文件夹内，对每个文件进行循环遍历
    os.rename(os.path.join(path_name,item),os.path.join(path_name,(str(name_list[j])+'.jpg')));#os.path.join(path_name,item)表示找到每个文件的绝对路径并进行拼接操作
    j=j+1
