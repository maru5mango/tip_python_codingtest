import datetime 
def solution(year, month, day):
  daylist=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT','SUN']
  return daylist[datetime.date(year, month, day).weekday()]
## import date time
#### datetime.date(year, month, date) => 날짜 형식으로 변환 
#### weekday() => 월요일은 0 / 숫자로 해당 날짜 요일 리턴


#for 문을 돌면서 값을 조금씩 바꾸어야 할 때 map 이용
target = [1, 2, 3, 4, 5]
result = list(map(lambda x : x+1, target))

import math
math.ceil() => 올림
math.floor() => 내림
round(num) => 반올림 ( 단 5일 경우에는 앞자리가 짝수면 내림, 홀수면 올림)

#문자열 길이 = len(s)
#문자열 자르기 => s[:2], s[-1:] 등 배열로 취급

#문자열 딕셔너리 이용하기
s_dic={}
s['a']=1
s['b']=2
s['c']=3

#d가 현재 딕셔너리에 없으므로 두번째 값인 'None'을 호출
s_dic.get('d', 'None')
s_dic={'a':1, 'b':2, 'c':3}

#d가 현재 딕셔너리에 없으므로 추가됨. d 값이 현재 있을 경우에는 뒤에 추가한 값이 무시됨.
s_dic.setdefault('d', 4)
