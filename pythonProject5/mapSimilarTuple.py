# This python program combines the tuples with similar first element
from collections import defaultdict

test_dict = [(1,2), (1,6), (2,3), (2,5), (3,8), (3,1), (3,2)]
print("The given original dictionary is:", str(test_dict))

mapp = defaultdict(list)
for key,val in test_dict:
    mapp[key].append(val)
res = [(key,*val) for key,val in mapp.items()]
print("The new dictionary is:", str(res))