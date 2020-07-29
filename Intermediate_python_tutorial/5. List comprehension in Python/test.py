#result = [value iteration filter]
'''
myList = []

for x in range(1, 11):
    myList.append(x**2)

print(list(myList))
'''

'''
myList = [ x**2 for x in range(1, 11) ]
print(list(myList))
'''

L = [3, 5, 2, 77,34, 12, 45]
odds = [ x for x in L if x%2 ]
print(list(odds))
