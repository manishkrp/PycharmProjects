# This program lists all the positive numbers
# in the given range
start,end = -4, 20

for num in range(start, end+1):
    if(num > 0):
        print(num, end = " ")
