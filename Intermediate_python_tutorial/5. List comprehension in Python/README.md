
#result = [value iteration filter]
'''
myList = []

for x in range(1, 11):
    myList.append(x**2)

print(list(myList))
'''

myList = [ x**2 for x in range(1, 11) ]
print(list(myList))


Python - test.py:12
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[Finished in 0.103s]





```
L = [3, 5, 2, 77,34, 12, 45]
odds = [ x for x in L if x%2 ]
print(list(odds))
```

Python - test.py:19
[3, 5, 77, 45]
[Finished in 0.104s]
