# This python program extracts the digits from a list

from itertools import chain

test_list = [(2,5), (6,21), (11,34)]

print("The original given list is:", str(test_list))

temp = map(lambda x: str(x), chain.from_iterable(test_list))
res = set()
for num in temp:
    for ele in num:
        res.add(ele)

print("The straightened list now is",str(res))