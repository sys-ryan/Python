map( ) : map every element of the given sequence object


```
myList = [1, 2, 3, 4, 5]
myList = map(float, myList)
print(list(myList))
```

Python - test.py:5
[1.0, 2.0, 3.0, 4.0, 5.0]
[Finished in 0.1s]



```
myList = [1, 2, 3, 4, 5]
myList = map(lambda x: x**2, myList)
print(list(myList))
```


Python - test1.py:5
[1, 4, 9, 16, 25]
[Finished in 0.112s]
