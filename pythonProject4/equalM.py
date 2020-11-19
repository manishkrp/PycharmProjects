# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def identicalMatrices(A,B):

    if A==B:
        print("Equal Matrices")

    else:
        print("not equal")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    A = [[1,2,3],
         [3,4,5],
         [7,8,9]]

    B = [[1,2,3],
         [3,5,5],
         [7,8,9]]

    identicalMatrices(A,B)