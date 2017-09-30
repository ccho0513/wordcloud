from konlpy.tag import Twitter
from collections import Counter

t = Twitter()
import csv
import codecs

text = codecs.open('silsigan_1000.txt','r','utf-8')
doc_ko = text.read()

# 단어 대체하기
replace_dic = {'추천':'','년':''}

def swap(document, dic):
    for Xword in document:
        if Xword in dic:
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
#print('Counter : ', FreqDict.most_common(100))

data = FreqDict.most_common(100)  #token 빈도값을 기준으로 내림차순으로 정리 ( most_common(n)을 하게 되면, 상위 n개의 빈도값과 token만을 의미 )

with codecs.open('words.csv', 'w', encoding='utf-8') as f:
    f.write('word,freq\n')
    writer = csv.writer(f)
    writer.writerows(data)



