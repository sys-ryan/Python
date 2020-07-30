```
def factorial(n):
    fact = []
    k = 1
    for i in range(1, n+1):
        k *= i
        fact.append(k)
    return fact

factorial(10)
```
[1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

메모리 사용 비요율적..


```
def factorial2(n):
    k = 1
    for i in range(1, n+1):
        k *= i
        yield k

f = factorial2(10)
type(f)
```
generator

```
next(f)
```
1

```
next(f)
```
2


--------------------------------------


```
natural_nos = [x**2 for x in range(1, 11)]
sum(natural_nos)
```
385

메모리 사용 비효율적...



```
natural_nos = (x**2 for x in range(1, 11))
type(natural_nos)
```
generator


```
sum(natural_nos)
```
385
