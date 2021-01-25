# This python program checks if the first
# character is a vowel or not
import re

regex = "^[aeiouAEIOU][A-Za-z0-9_]*"
def check(test_str):

    if(re.search(regex,test_str)):
        print("Accepted")
    else:
        print("Not Accepted")


# Driver program
if __name__ == "__main__()":
    test_str = "Damishk"
    check(test_str)

    test_str = "Allahabad"
    check(test_str)
