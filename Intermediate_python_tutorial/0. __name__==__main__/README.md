```
from myfunc import add

print(add(2, 2))
```

----------------------------------
출력 결과  

Python - test.py:3
5
4
[Finished in 0.12s]


myfunc 에서 호출된 메소드까지 함께 호출됨.

```
if __name__ == "__main__":
    print(add2(2, 3))
```

자기를 import 한 모듈이 아닌 자기 자신일 때만 호출되도록 함.

```
from myfunc2 import add2

print(add2(2, 2))
```

출력 결과  

Python - test.py:4
4
[Finished in 0.108s]
