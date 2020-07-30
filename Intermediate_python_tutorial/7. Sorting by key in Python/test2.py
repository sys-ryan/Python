record = [{'name': 'Nik', 'score': 9, 'age': 18},
          {'name': 'Rob', 'score': 8, 'age': 19},
          {'name': 'Sam', 'score': 8, 'age': 18},
          {'name': 'Harry', 'score': 6, 'age': 20}]



from operator import itemgetter

print( sorted(record, key = itemgetter('score', 'age')) )
