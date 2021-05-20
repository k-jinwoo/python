"""
날짜 : 2021/05/20
이름 : 김진우
내용 : 파이썬 데이터베이스 SQL 실습하기
"""

import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='192.168.10.114',user='kim415272',password='1234',db='kim415272',charset='utf8')

# SQL 실행 객체 생성
cur = conn.cursor()

# SQL 실행
sql = "UPDATE `USER1` SET `hp`='010-1111-1111' "
sql += "WHERE `uid`='p101';"
cur.execute(sql)
conn.commit()

# 데이터베이스 종료
conn.close()

print('Update 완료...')