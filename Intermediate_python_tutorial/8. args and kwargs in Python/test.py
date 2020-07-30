#fargs : formal arguments
#kwargs : keywords arguments
'''
def < func-name> (fargs, *args, **kwargs):
    <statements>
'''

def add(a, b):
    s = a + b;
    return s

print( add(2, 3) )

#위 함수의 경우 print( add(2, 3, 4, 5) ) 는 처리하지 못함.

# *args는 입력받은 arguments 를 tuple 로 바꿈.
def add_args(*nums):
    return sum(nums)

print(add_args(2, 3, 4, 5))

'''
출력 결과
14
'''




#**kwargs 는 입력받은 arguments를 dictionary로 바꿈
def record(**data):
    print(data)

record(name = "Nikhil", rollno = 85, age = 20)

'''
출력 결과
{'name': 'Nikhil', 'rollno': 85, 'age': 20}ㅠ
'''




def get_data(engine, *queries, **properties):
    print(engine, queries, properties)

get_data('google', 'python', 'flask', 'django', limit = 10, verbose = True)

'''
출력 결과
google ('python', 'flask', 'django') {'limit': 10, 'verbose': True}
'''
