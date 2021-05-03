"""
날짜 : 2021/05/03
이름 : 김진우
내용 : 파이썬 파일 입출력 실습 교재 p217
"""

# 파일 읽기(File Input)
file1 = open('C:/Users/bigdate/Desktop/Sample.txt', 'r') # open(열기) / r = read 읽기용(기본값)
line = file1.readline()

print('line :', line)
file1.close() # close(닫기)

# 여러줄 파일 읽기
file2 = open('C:/Users/bigdate/Desktop/Sample.txt', 'r')

while True :
    line = file2.read()

    if not line : # 읽을 라인이 없을 경우
        break

    print(line)

file2.close()

# 파일 쓰기(File Output)
file3 = open('C:/Users/bigdate/Desktop/Test.txt', 'w') # w = write 쓰기 / 파일이없고 가상경로 실행 시 파일생성
file3.write('안녕하세요.\n')
file3.write('반갑습니다.\n')
file3.write('감사합니다.\n')
file3.close()

# 구구단 쓰기
file4 = open('C:/Users/bigdate/Desktop/Gugudan.txt', 'w')
for i in range(2,10) :
    file4.write('---%d단---\n' % (i))
    for j in range(1,10) :
        file4.write('%d x %d = %d \n' % (i,j,i*j))
file4.close()