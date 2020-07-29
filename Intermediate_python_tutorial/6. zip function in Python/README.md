zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
※ 여기서 사용한 *iterable은 반복 가능(iterable)한 자료형 여러 개를 입력할 수 있다는 의미이다.

```
name = ['Nik', 'Rob', 'Sam', 'Harry']
age = [19, 20, 18, 19]
grade = ['A', 'B', 'A', 'C']


for x in zip(name, age, grade):
    print(x)
```


Python - test.py:7
('Nik', 19, 'A')
('Rob', 20, 'B')
('Sam', 18, 'A')
('Harry', 19, 'C')
[Finished in 0.111s]




```
myList = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

'''
(1, 5, 9)
(2, 6, 10)...
'''


for x in zip(*myList):
    print(x)
```



Python - test2.py:12
(1, 5, 9)
(2, 6, 10)
(3, 7, 11)
(4, 8, 12)
[Finished in 0.099s]
