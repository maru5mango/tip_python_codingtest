#큐 사용하기 list에 값이 있을 때 반복, 제일 왼쪽 값 기준 , 해당 조건이 맞으면 pop
while temp:
  c=temp.pop(0)
  count=1
  for i in range(len(temp)): //남은 큐에서 비교
    if c>=temp[0]:
      count+=1
      temp.pop(0)
    else:
      break

# pop 효율성 문제 -> deque 사용
from collections import deque
  dq=deque(리스트)
  len(dq)
  dq.popleft()
  dq.pop()
 

#우선순위 큐
from queue import PriorityQueue
que = PriorityQueue(maxsize=8)
#추가
que.put(3)
#삭제
que.get()
