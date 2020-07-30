'''
assert <condition>, <optional-message>
'''

def get_age(age):
    assert age > 0, "age can't be negative!"
    print("Ok yuor age is: ", age)


get_age(30)
