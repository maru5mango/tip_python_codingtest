#부분집합 구하기
def getSubset(lst):
    ans=[]
    n = len(lst)
    for i in range(1<<n):
      temp=[]
      for j in range(n): # j: 0001, 0010, 0100
          t_f = i & (1 << j)
          if t_f: 
              temp.append(lst[j])
      ans.append(temp)
    return ans
