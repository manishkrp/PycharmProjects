num= input("Enter the number:")
if(num>1):
    for(n in range(2,num)):
        if(n%2 ==0):
            print("number is not prime")

        else:
          print("number is a prime")


else:
    print("number is not prime")
