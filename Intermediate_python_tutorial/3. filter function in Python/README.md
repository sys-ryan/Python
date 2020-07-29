filter( )
filter 함수는 built-in 함수로 list 나 dictionary 같은 iterable 한 데이터를 특정 조건에 일치하는 값만 추출해 낼때 사용하는 함수이다.

```
myList = [1, 2, 3, 4, 5]
#filter( (testing condition), sequence object)
odds = filter((lambda x: x%2), myList)
print(list(odds))
```

Python - tset.py:7
[1, 3, 5]
[Finished in 0.116s]




```
myList2 = [1, -2, 3, -4, 5]
pos = filter((lambda x: x>0), myList2)
print(list(pos))
```

Python - tset.py:11
[1, 3, 5]
[Finished in 0.103s]
