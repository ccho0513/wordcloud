import sys
import sqlite3
from konlpy.tag import Twitter
from collections import Counter
import silsigan_crawling

silsigan_crawling.main()

t = Twitter()
import csv
import codecs

def get_data(result_list, cur) :
    sql = "select keyword1, keyword2, keyword3 from News order by ID desc LIMIT 1000;"
    cur.execute(sql)
    for row in cur :
        result_list.append(row[0])
        result_list.append(row[1])
        result_list.append(row[2])


# main func
def main():
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    result_list = []
    get_data(result_list, cur)
    FreqDict = Counter(result_list)
    # print('Counter : ', FreqDict.most_common(100))
    FreqDict[''] = 0  # FreqDict 안에 ''의 빈도수값을 0으로 바꿔버림
    data = FreqDict.most_common(50)  # token 빈도값을 기준으로 내림차순으로 정리 ( most_common(n)을 하게 되면, 상위 n개의 빈도값과 token만을 의미 )
    # data = data[1:51] #상위 2번째 부터 51번째까지만 들어갈 수 있도록 설정(필요없는 단어를 ''로 바꿀때, ''값이 너무 커져서 워드클라우드 생성 안되므로)

    with codecs.open('words.csv', 'w', encoding='utf-8') as f:
        f.write('word,freq\n')
        writer = csv.writer(f)
        writer.writerows(data)
    conn.close()


if __name__ == '__main__':
    main(sys.argv)