# This program checks if the given
# substring is in the start of given string or not
import re

def check(sample, string):

    if sample in string:
        y = "^" + sample

    x = re.search(y,string)
    if x:
        print("Yes")
    else:
        print("No")

#Driver program
if __name__ == "__main__":
    string = "geeks for geeks"
    sample = "geeks"
    check(sample,string)