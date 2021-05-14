secs = int(input('10000이상의 숫자를 입력하세요 : '))
hours = secs / 3600
mins = secs % 3600 / 60
sec = secs % 3600 % 60


print('시간은 %d %d %d' % (hours, mins, sec))