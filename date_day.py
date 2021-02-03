import datetime 
def solution(year, month, day):
  daylist=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT','SUN']
  return daylist[datetime.date(year, month, day).weekday()]

## import date time
#### datetime.date(year, month, date) => 날짜 형식으로 변환 
#### weekday() => 월요일은 0 / 숫자로 해당 날짜 요일 리턴
