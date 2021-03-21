# 입력
```pythone
import sys
## 정수
n=int(input())
a,b = map(int, sys.stdin.readline().split())

## 배열
arr = list(map(int,sys.stdin.readline().split()))

## 2차원 배열 n개
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

## 문자열 n줄 받아서 리스트로
data = [sys.stdin.readline().strip() for i in range(n)]
```

# 출력
소숫점 2째자리까지 출력
```pythone 
print(format(num, ".2f"))
```
