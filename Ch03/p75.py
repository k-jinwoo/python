"""
날짜 : 2021/04/28
이름 : 김진우
내용 : 실습 문장과 단어 추출 예 교재 p75
"""

string = """나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다."""

sents = [] # 문장 저장
words = [] # 단어 저장

# (1) 문단 -> 문장
for sen in string.split(sep = "\n") :
    sents.append(sen)
    # (2) 문장 -> 단어
    for word in sen.split() :
        words.append(word)

print('문장 : ', sents)
print('문장수 : ', len(sents))
print('단어 : ', words)
print('단어수 : ', len(words))