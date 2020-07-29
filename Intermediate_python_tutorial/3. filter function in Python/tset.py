myList = [1, 2, 3, 4, 5]

#filter( (testing condition), sequence object)

odds = filter((lambda x: x%2), myList)
print(list(odds))



myList2 = [1, -2, 3, -4, 5]
pos = filter((lambda x: x>0), myList2)
print(list(pos))
