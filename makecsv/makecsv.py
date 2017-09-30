from konlpy.tag import Twitter
from collections import Counter

t = Twitter()
import csv
import codecs

text = codecs.open('silsigan_1000.txt','r','utf-8')
doc_ko = text.read()

# 단어 대체하기
replace_dic = {'추천':'','년':''}

r0 = {'것':'','일':''}
r1 = {'등':'','이':''}
r2 = {'수':'','고':''}
r3 = {'안':'','날':''}
r4 = {'뒤':'','월':''}
r5 = {'만':'','말':''}
r6 = {'원':'','창':''}
r7 = {'쿵':'','전':''}
r8 = {'기자':'','씨':''}
r9 = {'그':'','위':''}
r10 = {'명':'','때':''}
r11 = {'를':'','억':''}
r12 = {'개':'','의':''}
r13 = {'중':'','더':''}
r14 = {'관련':'','며':''}
r15 = {'로':'','때문':''}
r16 = {'시':'','제':''}
r17 = {'건':'','이상':''}
r18 = {'곳':'','조':''}
r19 = {'이번':'','차':''}
r20 = {'우리':'','내':''}
r21 = {'팀':'','통해':''}
r22 = {'최근':'','점':''}

def swap(document, dic):
    for Xword in document:
        if Xword in dic:
            index = document.index(Xword)
            document[index] = document[index].replace(Xword, dic[Xword])
    return document

#token

def text2pos(silsigan):
    contentPos = []
    word_tag_pairs = t.pos(silsigan, norm=True, stem=True)
    keywords = [word for word, tag in word_tag_pairs if tag == 'Noun']
    contentPos.extend(keywords)
    return swap(contentPos, replace_dic)

token = text2pos(doc_ko)

token = swap(token, r0)
token = swap(token, r1)
token = swap(token, r2)
token = swap(token, r3)
token = swap(token, r4)
token = swap(token, r5)
token = swap(token, r6)
token = swap(token, r7)
token = swap(token, r8)
token = swap(token, r9)
token = swap(token, r10)
token = swap(token, r11)
token = swap(token, r12)
token = swap(token, r13)
token = swap(token, r14)
token = swap(token, r15)
token = swap(token, r16)
token = swap(token, r17)
token = swap(token, r18)
token = swap(token, r19)
token = swap(token, r20)
token = swap(token, r21)
token = swap(token, r22)

FreqDict = Counter(token)
#print('Counter : ', FreqDict.most_common(100))
FreqDict[''] = 0 #FreqDict 안에 ''의 빈도수값을 0으로 바꿔버림
data = FreqDict.most_common(50)  #token 빈도값을 기준으로 내림차순으로 정리 ( most_common(n)을 하게 되면, 상위 n개의 빈도값과 token만을 의미 )
#data = data[1:51] #상위 2번째 부터 51번째까지만 들어갈 수 있도록 설정(필요없는 단어를 ''로 바꿀때, ''값이 너무 커져서 워드클라우드 생성 안되므로)
with codecs.open('words.csv', 'w', encoding='utf-8') as f:
    f.write('word,freq\n')
    writer = csv.writer(f)
    writer.writerows(data)



