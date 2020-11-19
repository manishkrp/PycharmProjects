
num = 13


if num > 1:
    for n in range(2, num):
        if (num % n) == 0:
            print("number is not prime")
            break

    else:
        print("number is a prime")



else:
    print("number less than zero hence is not a prime")


