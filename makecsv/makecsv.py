
from konlpy.tag import Twitter
from collections import Counter

t = Twitter()
import csv
import codecs

text = codecs.open('silsigan_1000.txt','r','utf-8')
doc_ko = text.read()

# 단어 대체하기
replace_dic = {'바꿔야하는단어1': '바꿀단어1', '바꿔야하는단어2': '바꿀단어2'}

def swap(document, dic):
    for Xword in dic:
        if Xword in document:
            index = document.index(Xword)
            document[index]=document[index].replace(Xword, dic[Xword])
    return document

#token
def text2pos(silsigan):
    contentPos = []
    word_tag_pairs = t.pos(silsigan, norm=True, stem=True)
    keywords = [word for word, tag in word_tag_pairs if tag == 'Noun']
    contentPos.extend(keywords)
    return swap(contentPos, replace_dic)


token = text2pos(doc_ko)
FreqDict = Counter(token)

data = FreqDict.items()

with codecs.open('words.csv', 'w', encoding='utf-8') as f:
    f.write('word,freq\n')
    writer = csv.writer(f)
    writer.writerows(data)



