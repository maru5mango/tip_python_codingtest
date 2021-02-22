import heapq

#힙 추가하기
heap=[]
heapq.heappush(heap, 1)

#힙 삭제하기
heapq.heappop(heap) -> 최솟값 pop

#힙 최솟값 보기
heap[0]

#리스트를 힙으로
tmp = [7, 5, 8, 3]
heapq.heapify(tmp)


#우선 순위가 포함된 힙(튜플 사용하기)
import heapq

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(heapq.heappop(heap)[1])  # index 1

  
 #가장 큰 값 지우기
que=heapq.nsmallest(len(que)-1,que)
#가장 큰 값 가져오기( 삭제되지는 않음 )
max_num=heapq.nlargest(1,que)
