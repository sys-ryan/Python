reduce( )
파이썬의 functools 내장 모듈의 reduce() 함수는 여러 개의 데이터를 대상으로 주로 누적 집계를 내기 위해서 사용합니다.
기본 문법은 다음과 같은데요. 기본적으로 초기값을 기준으로 데이터를 루프 돌면서 집계 함수를 계속해서 적용하면서 데이터를 누적하는 방식으로 작동합니다.
```
reduce(집계 함수, 순회 가능한 데이터[, 초기값])
```


```
from functools import reduce

myList = [1, 2, 3, 4, 5]

#reduce( funciton, sequence object)

prod = reduce( (lambda x, y : x*y), myList)

print(prod)
```

//process
1 1 = 1
2 1 = 2
3 2 = 6
4 6 = 24
5 24 = 120



Python - test.py:10
120
[Finished in 0.1s]



```
from functools import reduce

myList = [1, 2, 3, 4, 5]
greatest = reduce ( (lambda x, y : y if (y>x) else x), myList)
print(greatest)
```


Python - test.py:16
5
[Finished in 0.116s]
