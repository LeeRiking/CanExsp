 # -*- coding: utf-8 -*-
"""
Created on Sat May 11 21:34:38 2019

@author: THINK
"""

import os
import os.path
import numpy as np
from sklearn.feature_extraction.text import HashingVectorizer 
import xlwt
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
import xlrd
import csv
from datetime import datetime
from dateutil import parser
import math

# 卡方计算公式
def ChiCalc(A, B, C, D):
    if  float((A+C) * (A+B) * (B+D) * (C+D)) == 0:
        result = 10000
    else:
        result = float(pow((A*D - B*C), 2)) /float((A+C) * (A+B) * (B+D) * (C+D))
    return result


data = xlrd.open_workbook(r'C:\Users\THINK\Desktop\笔记\自然语言处理\保留词语.xlsx')
f1 = open(r'C:\Users\THINK\Desktop\笔记\自然语言处理\合并文本的时序索引.csv')
news_data = pd.read_csv(f1)#不能带有中文名字

vocabulary = data.sheets()[0]
vocabulary = vocabulary.col_values(0)
rootdir = r'C:\Users\THINK\Desktop\笔记\自然语言处理\合并非工作日txt'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件,将文件夹下文件堪称列表
news_list = []
for k in range(0, len(list)):
#for k in range(0, 5):
    path = os.path.join(rootdir, list[k])
    if os.path.isfile(path):
        news = open(path, "r", encoding='UTF-8').read()
        news_list.append(news)
news_data['content']=news_list  #转化在一个dataframe中
#提取卡方分析中四表格所需数据
classTerm_count_CHI = dict()    #记录卡方值字典
for eachword in vocabulary:   
#对每一类分别进行四表格统计    
#对于每篇文章，四表格初始化
    A = 0
    B = 0
    C = 0
    D = 0
    for ipapers in range(0,len(news_data['label'])):
        if news_data['label'][ipapers] == 1:        
            if eachword in news_data['content'][ipapers]:
                A = A + 1
            else:
                C = C + 1
        else:                   
            if eachword in news_data['content'][ipapers]:
                B = B + 1
            else:
                D = D + 1
    classTerm_count_CHI[eachword] = ChiCalc(A,B,C,D)
sortedclassTerm_count_CHI = sorted(classTerm_count_CHI.items(), key=lambda d:d[1], reverse=True)
#        count = 0
subDic = dict()
########取前K个最大卡方值词组成的词典
K=900
for i in range(K):
    subDic[sortedclassTerm_count_CHI[i][0]] = sortedclassTerm_count_CHI[i][1]
#        termCountDic[key] = subDic       
            
        