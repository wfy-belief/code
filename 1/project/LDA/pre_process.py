# -*- coding:utf-8

'''

preprocess.py
这个文件的作用是做文档预处理，
讲每篇文档，生成相应的token_list
只需执行最后documents_pre_process函数即可。

'''
import re
import traceback
from collections import defaultdict

import jieba
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
from nltk.tokenize import WordPunctTokenizer

# 分词 - 英文


def tokenize(document):
    try:
        # 对文档的英文单词进行分词
        token_list = WordPunctTokenizer().tokenize(document)
        #print("[INFO]: tokenize is finished!")
        # 返回英语词汇列表
        return token_list

    except Exception as e:
        # print_exc是简化版的print_exception,
        # 由于exception type, value和traceback object
        # 都可以通过sys.exc_info()获取，因此print_exc()
        # 就自动执行exc_info()来帮助获取这三个参数
        print(traceback.print_exc())

# 分词 - 中文


def tokenize_chinese(document):
    try:
        # 中文进行分词，返回分组的列表
        token_list = jieba.cut(document, cut_all=False)

        #print("[INFO]: tokenize_chinese is finished!")
        return token_list

    except Exception as e:
        print(traceback.print_exc())

# 去除停用词 -英文


def filtered_stopwords_en(token_list):
    try:
        # 过滤停用词，保留非停用词
        token_list_without_stopwords = [
            word for word in token_list if word not in stopwords.words("english")]

        #print("[INFO]: filtered_words is finished!")
        return token_list_without_stopwords
    except Exception as e:
        print(traceback.print_exc())

# 去除停用词 - 中文


def filtered_stopwords_ch(token_list, stopwords):
    try:
        # 过滤停用词，保留非停用词
        token_list_without_stopwords = [
            word for word in token_list if word not in stopwords]

        # print("[INFO]: filtered_words is finished!")
        return token_list_without_stopwords
    except Exception as e:
        print(traceback.print_exc())


# 去除标点
def filtered_punctuations(token_list):
    try:
        # 定义标点符号簇，然后过滤标点，保留非标点字符
        punctuations = ['', '\n', '\t', ',', '.', ':', ';', '?',
                        '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%', 'xa0', '，']
        token_list_without_punctuations = [
            word for word in token_list if word not in punctuations]

        #print("[INFO]: filtered_punctuations is finished!")
        return token_list_without_punctuations

    except Exception as e:
        print(traceback.print_exc())

# 过滤出中 - 英文


def filtered_chinese_english_words(token_list):
    try:
        # 构造字母数字下划线匹配器
        r1 = re.compile(r'\w')  # 使用正则表达式,筛选[A-Za-z0-9_]
        # 构造非数字正则匹配器
        r2 = re.compile(r'[^\d]')  # 使用正则表达式,筛选[0-9_]
        # 构造非下划线正则匹配器
        r4 = re.compile(r'[^_]')
        # 构造中文字符正则匹配器
        r3 = re.compile(r'[\u4e00-\u9fa5]')
        # 筛选出来中英文字词列表
        token_list = [word.lower() for word in token_list if (r3.match(word) != None) or (
            r3.match(word) == None and r1.match(word) and r2.match(word) and r4.match(word))]
        # print("[INFO]: filtered_punctuations is finished!")
        return token_list

    except Exception as e:
        print(traceback.print_exc())

# 词干化 -英文


def stemming(filterd_token_list):
    try:
        # 基于Lancaster 词干提取算法，Stemming 可以抽取词的词干或词根形式
        st = LancasterStemmer()
        # 提取词干
        stemming_token_list = [st.stem(word) for word in filterd_token_list]

        #print("[INFO]: stemming is finished")
        return stemming_token_list

    except Exception as e:
        print(traceback.print_exc())

# 去除低频单词


def low_frequence_filter(token_list):
    try:
        # 通过python的collections里面的方法
        # 产生关键词词频的统计
        # 类似的方法有Counter同样可以进行统计
        # Counter直接产生结果
        word_counter = defaultdict(int)
        for word in token_list:
            word_counter[word] += 1

        # 设置阈值
        threshold = 0
        # 过滤阈值以下元素
        token_list_without_low_frequence = [word
                                            for word in token_list
                                            if word_counter[word] > threshold]

        # print "[INFO]: low_frequence_filter is finished!"
        return token_list_without_low_frequence
    except Exception as e:
        print(traceback.print_exc())


"""
功能：预处理
@ document: 文档
@ token_list: 预处理之后文档对应的单词列表
"""


def pre_process(document, ch_stopwords):
    try:

        # token_list = tokenize(document)
        # 对每篇文档进行中文分词
        token_list = tokenize_chinese(document)
        # 对每篇文档过滤出中英文
        token_list = filtered_chinese_english_words(token_list)
        # 对每篇文档过滤出中问停用词
        token_list = filtered_stopwords_ch(token_list, ch_stopwords)
        # 对每篇文档过滤标点
        token_list = filtered_punctuations(token_list)

        #print("[INFO]: pre_process is finished!")
        return token_list

    except Exception as e:
        print(traceback.print_exc())


"""
功能：预处理
@ document: 文档集合
@ token_list: 预处理之后文档集合对应的单词列表
"""


def documents_pre_process(documents, ch_stopwords):
    try:

        documents_token_list = []
        for document in documents:
            token_list = pre_process(document, ch_stopwords)
            documents_token_list.append(token_list)

        print("[INFO]:documents_pre_process is finished!")
        return documents_token_list

    except Exception as e:
        print(traceback.print_exc())

# -----------------------------------------------------------------------


def test_pre_process(documents, ch_stopwords):

    # documents = ["he,he,he,we are happy!",
    #              "he,he,we are happy!",
    #              "you work!"]
    documents_token_list = []
    for document in documents:
        token_list = pre_process(document, ch_stopwords)
        documents_token_list.append(token_list)

    for token_list in documents_token_list:
        print(token_list)


# test_pre_process()
# 输入文件路径
'''
INPUT_PATH = "/data/python_pj6/bigdata"
# 加载停用词
ch_stopkeyword = [line.strip() for line in open(
    '/data/python_pj6/stopword').readlines()]
# 读取文件
data = pd.read_csv(INPUT_PATH)
# 测试预处理功能
test_pre_process(data.岗位描述, ch_stopkeyword)
'''