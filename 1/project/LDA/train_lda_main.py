# -*- coding:utf-8

'''
train_lda_main.py
这个文件的作用是汇总前面各部分代码，对文档进行基于lda的相似度计算

'''

import traceback

import pandas as pd

from lda_model import get_lda_model
from save_result import save_similarity_matrix
from similarity import lda_similarity_corpus

INPUT_PATH = "/data/python_pj6/bigdata"
OUTPUT_PATH = "/data/python_pj6/lda_simi_matrix.txt"
# data=pd.read_csv(INPUT_PATH)
# print(data.岗位描述)
# print(data.info())


def train(documents, stopword):
    try:

        # 语料
        # documents = ["Shipment of gold damaged in a fire",
        #              "Delivery of silver arrived in a silver truck",
        #              "Shipment of gold arrived in a truck"]

        # 训练lda模型
        K = 2  # number of topics
        lda_model, _, _, corpus_tf, _ = get_lda_model(documents, 50, stopword)

        # 计算语聊相似度
        lda_similarity_matrix = lda_similarity_corpus(corpus_tf, lda_model)

        # 保存结果
        save_similarity_matrix(lda_similarity_matrix, OUTPUT_PATH)
        return lda_similarity_matrix

    except Exception as e:
        print(traceback.print_exc())


def main(document):
    INPUT_PATH = "/data/python_pj6/bigdata"
    data = pd.read_csv(INPUT_PATH)
    stopword = [line.strip() for line in open(
        '/data/python_pj6/china_stopword').readlines()]  # 加载停用词
    frames = [document, data]
    df = pd.concat(frames)
    # print(df)
    similiry = train(df.岗位描述, stopword)
    for index, simi in enumerate(similiry[0]):
        if simi > 0.99:
            print(data[index:index+1][['工作名称', '公司名称', '岗位描述']])
            # print(index,'---',simi)

'''
test_data = pd.read_csv('/data/python_pj6/test_data')
main(test_data)
'''