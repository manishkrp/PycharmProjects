# This program prepares all possible
# combinations of two tuples

test1 = (1, 2)
test2 = (3, 4)

res = [(x, y) for x in test1 for y in test2]
res = res + [(x, y) for x in test2 for y in test1]

print("The combinations we get: ", str(res))