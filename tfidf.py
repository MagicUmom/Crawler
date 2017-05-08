from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from os.path import isfile, join
from optparse import OptionParser
import os
import jieba
import math
import sys

parser = OptionParser()
parser.add_option("-d", "--DIR", dest="dir", help="write dir name to read", metavar="DIR")
parser.add_option("-m", "--MODE", dest="mode", help="mode 0 / mode 1 : default / output for textcloud", metavar="MODE",default=0)
parser.add_option("-t", "--THRESHOLD", dest="threshold", help="default is 0 ", metavar="THRESHOLD" ,default=0)

(options, args) = parser.parse_args()


def test():
    return

def search_file_in_dir(dir):
    mypath  = os.getcwd() +"/"+str(dir)
    # print(mypath)
    onlyfiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
    return (onlyfiles)

def tf_idf(corpus):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    word = vectorizer.get_feature_names()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(X)

    weight = tfidf.toarray()
    for i in range(len(weight)):
        if (options.mode) == 0:
            print( u"-------輸出第",i,u"文本詞語的tf-idf權重------")
            for j in range(len(word)):
                if weight[i][j]> float(options.threshold):
                    print( word[j],weight[i][j]  )
        else:
            for j in range(len(word)):
                if weight[i][j]> float(options.threshold):
                    print(int(math.sqrt(weight[i][j]) * 10), word[j])


def main():

    word_list = []
    for i in search_file_in_dir(options.dir):
        mypath = os.getcwd() +"/"+ options.dir +"/"+str(i)
        f = open(mypath,"r")
        word=[]
        for x in jieba.cut(f.read()) :
            word.append(x)
        word_list.append(" ".join(word))
    # print(word_list)
    tf_idf(word_list)


if __name__ == '__main__':
    main()
    # search_file_in_dir()
    # test()