# (name, score, age)

record = [('Nik',   9, 18),
          ('Rob',   8, 19),
          ('Sam',   8, 18),
          ('Harry', 6, 20)]


#첫 번째 element 기준으로 정렬
print(sorted(record))


# index 1 element 기준으로 정렬
from operator import itemgetter

k = itemgetter(1)
print(list(map(k, record)))


# index 2 element 기준으로 정렬
print(sorted(record, key = itemgetter(2)))


# score 기준으로 정렬 & age 기준으로 정렬
print(sorted(record, key = itemgetter(1, 2)))
