# 소수 판별 알고리즘
import math

def is_prime_num(n):
  for i  in range(2, int(math.sqrt(n))+1):
    if n%i==0:
      return False
  return True
