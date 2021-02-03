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
  
#삽입정렬, 적당한 위치를 찾아서 넣는다.
def insertionSort(x):
  for i in range(1,len(x)):
    j, key = i -1, x[i]
    while x[j] > key and j >= 0:
      x[j+1] = x[j]
      j = j - 1
      x[j+1] = key
  return x
