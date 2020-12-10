# -*- coding:utf-8
'''
save_result.py
这个文件的作用是保存结果
'''


import traceback


def save_similarity_matrix(matrix, output_path):
    try:
        # 写模式打开文件，没有则创建
        outfile = open(output_path, "w")
        # 写入内容
        for row_list in matrix:
            line = ""
            for value in row_list:
                line += (str(value) + ',')
            outfile.write(line + '\n')
        # 从系统IO关闭文件读进程
        outfile.close()
        print("[INFO]:save_similarity_matrix is finished!")
    except Exception as e:
        # print_exc是简化版的print_exception,
        # 由于exception type, value和traceback object
        # 都可以通过sys.exc_info()获取，因此print_exc()
        # 就自动执行exc_info()来帮助获取这三个参数
        print(traceback.print_exc())
