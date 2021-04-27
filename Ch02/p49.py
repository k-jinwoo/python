"""
날짜 : 2021/04/27
이름 : 김진우
내용 : 실습 문자열 색인과 연산 예 교재 p49
"""

# (1) 문자열 색인
string = "PYTHON"
print(string[0])
print(string[5])
print(string[-1])
print(string[-6])

# (1) 문자열 연산
print("python" + "program") # 결합 연산자
#print("python-" + 3.7 + ".exe" # error
print("python-" + str(3.7) + ".exe") # python-3.7.exe

print("-"*30) # 반복연산자