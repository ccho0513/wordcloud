from konlpy.tag import Twitter
from collections import Counter

t = Twitter()
import csv
import codecs

text = codecs.open('silsigan_10.txt','r','utf-8')
doc_ko = text.read()

# 단어 대체하기
replace_dic = {'추천':'','때문':'','관련':'','대한':''}

def swap(document, dic):
    for Xword in document:
        if len(Xword)==1: #단어의 길이가 1일 경우
            index = document.index(Xword)
            document[index] = document[index].replace(Xword,'') #단어삭제
        elif Xword in dic: #그외의 경우
            index = document.index(Xword)
            document[index] = document[index].replace(Xword, dic[Xword]) #대체가능한 단어 적은 것중에서 실행
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
FreqDict[''] = 0 #FreqDict 안에 ''의 빈도수값을 0으로 바꿔버림
data = FreqDict.most_common(50)  #token 빈도값을 기준으로 내림차순으로 정리 ( most_common(n)을 하게 되면, 상위 n개의 빈도값과 token만을 의미 )
#data = data[1:51] #상위 2번째 부터 51번째까지만 들어갈 수 있도록 설정(필요없는 단어를 ''로 바꿀때, ''값이 너무 커져서 워드클라우드 생성 안되므로)

with codecs.open('words.csv', 'w', encoding='utf-8') as f:
    f.write('word,freq\n')
    writer = csv.writer(f)
    writer.writerows(data)



