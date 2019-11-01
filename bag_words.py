# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:39:15 2019

@author: THINK
"""
import jieba
#jieba.load_userdict('F:/爬虫/my_dict.txt')
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import os.path
import jieba.analyse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn.feature_extraction.text import HashingVectorizer 
import xlwt
import pandas as pd


rootdir = 'C:/Users/THINK/Desktop/上证综指文本数据/SZ50/'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
news_list = []
for k in range(0, len(list)):
#for k in range(0, 5):
    path = os.path.join(rootdir, list[k])
    if os.path.isfile(path):
        news = open(path, "r", encoding='UTF-8').read()
        news_list.append(news)
all_list= ['  '.join(jieba.cut(s,cut_all = False)) for s in news_list]

#从文件导入停用词表
stpwrdpath = "F:/爬虫/stop_words/stop_words.txt"
stpwrd_dic = open(stpwrdpath, 'rb')
stpwrd_content = stpwrd_dic.read()
stpwrdlst = stpwrd_content.splitlines()
# 哈希向量化（降维版）
vectorizer = HashingVectorizer(n_features = 720)
vector = vectorizer.transform(all_list).toarray()
# 词袋模型向量化（降维版）
#tfidf=TfidfVectorizer(stop_words=stpwrdlst)
#weight=tfidf.fit_transform(all_list).toarray()
#word=tfidf.get_feature_names()
#print ('IFIDF词频矩阵:\n')
#print (weight) 
#for i in range(len(weight)): # 打印每个文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一个文本下的词语权重
#    print ("-------这里输出第", i, "个文本的词语tf-idf权重------")
#    for j in range(len(word)):
#        print(word[j], weight[i][j]) #第i个文本中，第j个词的tfidf值

#使用pandas将数组导出EXCEL
data_df = pd.DataFrame(vector)

 
# 保存文件
data_df.to_csv('C:/Users/THINK/Desktop/上证综指文本数据/文档矩阵.csv')