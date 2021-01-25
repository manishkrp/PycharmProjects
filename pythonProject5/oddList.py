# This program lists the odd elements of the given list
test_list = [1, 2, 3, 4, 5, 6, 7]

print("The given list is:", str(test_list))

for num in test_list:
    if(num % 2 != 0):
        print(num, end=" ")
