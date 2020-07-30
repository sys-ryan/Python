```
data = {
    'a': [1, 2, 3],
    'b': "kakao talk",
    (1, 2): [1, 2]
}

import pickle

with open("test.pkl", "wb") as f:
    pickle.dump(data, f)

del data

data
```


---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-7-c5d84736ba45> in <module>
----> 1 data

NameError: name 'data' is not defined


```
with open("test.pkl", "rb") as f:
    data = pickle.load(f)

data
```
{'a': [1, 2, 3], 'b': 'kakao talk', (1, 2): [1, 2]}


```
class Fruit:
    def __init__(self, name):
        self.name = name
        if name == "banana":
            self.color = "yellow"
        else:
            self.color = "unknown"

myfruit = Fruit("banana")

pickle.dump(myfruit, file=open("test.pkl", "wb"))
del myfruit
myfruit
```

---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-17-8b2ec94955eb> in <module>
----> 1 myfruit

NameError: name 'myfruit' is not defined


```
myfruit = pickle.load(file = open("test.pkl", "rb"))
myfruit
```
<__main__.Fruit at 0x7d2090>


```
myfruit.color
```
'yellow'

```
pickle.dump(myfruit, file=open("test.pkl", "wb"), protocol = pickle.HIGHEST_PROTOCOL)
```

*** There are many Protocol versions for pickle. (ref. python 3 library - pickle)
