# This python program returns the biggest anagram string
# in the given string

from collections import Counter

def maxAnaStr(input):

    input = input.split(" ")

    lenDict = Counter(input)

    for i in range(0,len(input)):
        input[i] = ''.join(sorted(input[i]))

    print(max(lenDict.values()))

# Driver program
if __name__=="__main__()":
    input = 'ant magenta magnate tan gnamate'
    maxAnaStr(input)
