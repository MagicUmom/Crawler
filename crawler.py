from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import os
import ssl
def writeInFile(contents,fileName,dirName):
    path = os.getcwd()+"/"+str(dirName)+"/"+str(fileName)+".txt"
    f = open(path,"w")
    f.write(contents)

def get_content(soup,fileName,dirName):
    i=0
    for tag in soup.find_all(attrs={"class": "single-post-content"}):

        #   del tag['blockquote']
        # print(tag["blockquote"])
        # del tag["single-post-content-sig"]
        # print("{0}".format(tag))
        writeInFile(tag.get_text(),i+fileName*10,dirName)
        i+=1
        # print("-----------------")

def get_max_page(soup):
    return int(soup.find_all(attrs={"class","pagination"})[2].find_all("a")[-1].get_text())

def crawler(url , context , page_count , dirName):
    page = urlopen(url , context=context)
    contents = page.read()
    soup = BeautifulSoup(contents, "html.parser")

    get_content(soup,page_count,dirName)


def main():
    if len(sys.argv) < 2:
        url = "https://www.mobile01.com/topicdetail.php?f=651&t=4797903&p=1"
    else :
        try :
            f = open(sys.argv[1],"r")
            url = str(f.readline())
        except :
            print("No File Exist !")
            exit(1)
    # print(url)
    context = ssl._create_unverified_context()

    try :
        page = urlopen(url , context=context)
        contents = page.read()
        soup = BeautifulSoup(contents, "html.parser")

        # dirName & number of pages
        dirName = soup.find(attrs={"class": "topic"}).get_text()
        pages_num = get_max_page(soup)

        # create dir
        if not os.path.exists(dirName):
            os.makedirs(dirName)
        for i in range(pages_num):
            url = url[:-1] + str(i+1)
            crawler(url , context ,i ,dirName)
            print(url)
    except :
        print("the page isn't exist !")


if __name__ == '__main__':
    main()
