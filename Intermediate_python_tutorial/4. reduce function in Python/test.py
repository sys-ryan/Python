from functools import reduce

myList = [1, 2, 3, 4, 5]

#reduce( funciton, sequence object)

prod = reduce( (lambda x, y : x*y), myList)
print(prod)


greatest = reduce ( (lambda x, y : y if (y>x) else x), myList)
print(greatest)
