# product
```python
from itertools import product
l = [(x, -x) for x in numbers]
s = list(product(*l))
```
곱집합 구하기 : 각각 원소를 하나씩 고른 순서쌍 ex. 좌표 평면 위의 점   
' * ' 표시: 파라미터를 몇 개 받을 지 모름


# combination
```python
from itertools import combinations
list(combinations(nums,3))
```
