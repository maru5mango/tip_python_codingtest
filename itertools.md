# product
```python
from itertools import product
l = [(x, -x) for x in numbers]
s = list(product(*l))
```
곱집합 구하기 : 각각 원소를 하나씩 고른 순서쌍 ex. 좌표 평면 위의 점
