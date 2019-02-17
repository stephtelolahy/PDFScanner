import os
import sys
import re
import time
import PyPDF2
import collections


def getPagesCount(pdf_file):
    pdfFileObj = open(pdf_file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pages = pdfReader.numPages
    return pages


def extractText(pdf_file, page):
    pdfFileObj = open(pdf_file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(page)
    data = pageObj.extractText()
    return data


def extractWords(pdf_file):
    allWords = []
    numPages = getPagesCount(pdf_file)
    for i in range(numPages):
        text = extractText(pdf_file, i)
        words = text.split()
        for j in words:
            allWords.append(j)
    return allWords


def arrayToDictionary(array):
    counter = collections.Counter(array)
    ordered = collections.OrderedDict(sorted(counter.items(), key=lambda t: t[1]))
    result = collections.OrderedDict(reversed(list(ordered.items())))
    return result


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
        # print(allWords)

        # create words occurences
        wordOccurences = arrayToDictionary(allWords)
        for (key, value) in wordOccurences.items():
            print(value, key)


if __name__ == '__main__':
    main()
