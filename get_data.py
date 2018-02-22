# encoding:utf-8

import os
import sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")

path = os.getcwd() + '/data/'  #原始数据
path1 = os.getcwd() + '/title_abs/'  #处理后的标题和摘要

if not os.path.exists(path1):
    os.mkdir(path1)

filelist = os.listdir(path)  #取得当前路径下的所有文件

def get_title_abs():
    abstracts = []

    for files in filelist:
        filename = os.path.splitext(files)[0]  #取文件名
        soup = BeautifulSoup(open(path + filename + '.xml'), 'html.parser')  #解析网页
        abstract = soup.find("p", class_="abstracts")  #取得"p",class="abstracts"的内容

        if abstract is None or abstract.string is None:
            continue
        else:
            abstracts.extend(soup.title.stripped_strings)
            s = abstract.string
            abstracts.extend(s.encode('utf-8'))

            with open(path1 + filename + ".txt", "w+") as f:
                for i in abstracts:
                    f.write(i)

            abstracts = []

if __name__ == '__main__':
    get_title_abs()
