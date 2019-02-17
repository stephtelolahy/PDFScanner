import os
import sys
import re
import time
import PyPDF2


def getPageCount(pdf_file):
    pdfFileObj = open(pdf_file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pages = pdfReader.numPages
    return pages


def extractData(pdf_file, page):
    pdfFileObj = open(pdf_file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(page)
    data = pageObj.extractText()
    return data


def getWordCount(data):
    data = data.split()
    return len(data)


def getWords(data):
    return data.split()


def extractWords(pdf_file):
    allWords = []
    numPages = getPageCount(pdf_file)
    for i in range(numPages):
        text = extractData(pdf_file, i)
        words = getWords(text)
        for j in words:
        	allWords.append(j)
    return allWords

def main():
    if len(sys.argv) != 2:
        print('command usage: python word_count.py FileName')
        exit(1)
    else:
        pdfFile = sys.argv[1]

        # check if the specified file exists or not
        try:
            if os.path.exists(pdfFile):
                print(pdfFile, " found !")
        except OSError as err:
            print(err.reason)
            exit(1)

        # get the words in the pdf file
        allWords = extractWords(pdfFile)
        time.sleep(1)
        print(allWords)


if __name__ == '__main__':
    main()
