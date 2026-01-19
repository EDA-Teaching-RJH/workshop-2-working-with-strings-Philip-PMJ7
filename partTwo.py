import math  

def main():
    A = int(input("What is the first length? (INT)"))
    B = int(input("What is the second length? (INT)"))
    C = pythag(A,B)
    print(C)

def pythag(A,B):
    A2 = A ** 2
    B2 = B ** 2

    C2 = A2 + B2
    C = math.sqrt(C2)
    return C

main()
