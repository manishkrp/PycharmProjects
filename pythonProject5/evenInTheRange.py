# This program lists the even numbers in the given range

start, end = 4, 15

for num in range(start, end+1):
    if(num % 2 == 0):
        print(num, end = " ")
