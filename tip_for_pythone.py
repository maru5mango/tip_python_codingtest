import datetime 
def solution(year, month, day):
  daylist=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT','SUN']
  return daylist[datetime.date(year, month, day).weekday()]
## import date time
#### datetime.date(year, month, date) => 날짜 형식으로 변환 
#### weekday() => 월요일은 0 / 숫자로 해당 날짜 요일 리턴

new_list=list(map(list, zip(*board))) -> 행열을 바꿈
new_list[a]=[i for i in new_list[a] if i!=0] -> 0인 값을 없애버리기

enumerate(list, start=1) => 인덱스랑 해당 내용 튜플로 묶기

#문자열 자르기
s.split(' '):
  
#첫글자만 대문자
s.capitalize()
s.title()

#문자열 붙이기
''.join(ans)


#리스트 내용 갯수 세서 딕셔너리 
closet={}
    for i in [x[1] for x in clothes]:
      try: closet[i]+=1
      except: closet[i]=1
#리스트 내용 갯수 세서 반환
from collections import Counter        
cnt = Counter([kind for name, kind in clothes])
cnt.most_common() -> 제일 빈도 수 높은 것 부터 튜플로 

#인덱스 에러
 a[-1:]  -> 빈 배열도 가능
  
max(b) => 배열 b중 가장 큰 값 찾기


#튜플 두번째 값으로 정렬
v.sort(key=lambda x:x[1])

#sort여러개
v.sort(key=lambda x: (int(x[0]), len(x[1])))

#for 문을 돌면서 값을 조금씩 바꾸어야 할 때 map 이용
target = [1, 2, 3, 4, 5]
result = list(map(lambda x : x+1, target))
result = list(filter(lambda x : x%2==0, target))

#map, filter, lambda
# 리스트 여러개를 묶어 결과 값을 도출 할 때 map
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
>>> list(map(lambda x, y: x * y, a, b))

# 해당 조건이 참인 것만 골라낼 때 filter
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
>>> list(filter(lambda x: x > 5 and x < 10, a))

# 리스트 a를 함수 f를 반복해서 해야하는 경우
import functools
a = [1, 2, 3, 4, 5]
print(functools.reduce(lambda x, y: x * y, a))

# 인덱스 에러 날 때
arr[x]!=arr[x+1] => [arr[x]]!=arr[x+1:x+2]

#파이썬에서 문자열에서 특정 문자 찾기
s.lower() => s.count('p')

#인덱스랑 리스트 요소 중 작은 것 출력
map(min, enumerate(list, start=1))

#파이썬 숫자를 문자열로
str(n)

#파이썬 문자열 배열을 숫자 배열로
list(map(int,s))

#파이썬 배열 뒤집어 출력, reversed()도 있음
list
list.reverse()
print(list)

#큰 순서대로 정렬
list.sort(reverse=True) 

import math
math.ceil() => 올림
math.floor() => 내림
round(num) => 반올림 ( 단 5일 경우에는 앞자리가 짝수면 내림, 홀수면 올림)
from math import gcd
#최대 공약수
a=gcd(a,b)
#최소 공배수
a=a*b//gcd(a,b)

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

#values값들로 리스트 만들기
temp=[i for i in dic.values()]

#키 값들로 리스트 만들기
key=[i for i in dic.keys()]

#리스트를 딕셔너리로 만들기( 키 값으로 쓰기 )
 x = dict.fromkeys(keys)
  
#이차원 배열 딕셔너리로 만들기
x=dict(list)

