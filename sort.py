#간단한 정렬 버블 정렬 , 인접한 두 원소 비교하여 위치 스왑
def bubble(x):
  for i in range(len(x)-1):
    for j in range(len(x) - i):
      if x[j] > x[j+1]:
        x[j], x[j+1] = x[j+1], x[j] 
  return x
  
#퀵정렬// 재귀를 이용함.  
def quickSort(x):
  if len(x) <= 1:
    return x
  pivot = x[len(x)//2]
  left,right,equal =[],[],[]
  for a in x:
    if a < pivot:
      left.append(a)
    elif a > pivot:
      more.append(a)
    else:
      equal.append(a)
  return quickSort(left) + equal + quicksort(right)

def quickSort(a, start, end):# 재귀함수용 함수 선언(리스트, 시작인덱스, 종료인덱스)
    # print(a)
    if start < end: # 시작 인덱스 보다 끝 인덱스가 클 경우
        left = start # left 변수에 시작 인덱스 할당
        pivot = a[end] #  //pivot 값은 a리스트에 마지막 원소 값
        for i in range(start, end): # 시작인덱스부터 끝 원소까지 반복
            if a[i] < pivot: # 리스트 인덱스 값이 pivot 값보다 작을 경우라면
                a[i], a[left] = a[left], a[i] #  해당 인덱스와 left인덱스  swap
                left += 1 # 인덱스 하나 증가 시켜주기(자리를 옮겨가며 비교해야 하기 때문에)
        a[left] , a[end] = a[end], a[left] # left인덱스와 끝 인덱스 swap
        print(left)
        quickSort(a, start, left-1) # 재귀 호출 (리스트, 시작 인덱스, left-1)
        quickSort(a, left+1, end) # 재귀 호출 (리스트, left+1, 종료인덱스)
  
#삽입정렬, 적당한 위치를 찾아서 넣는다.
def insertionSort(x):
  for i in range(1,len(x)):
    j, key = i -1, x[i]
    while x[j] > key and j >= 0:
      x[j+1] = x[j]
      j = j - 1
      x[j+1] = key
  return x
