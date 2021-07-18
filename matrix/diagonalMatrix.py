# Element where the only the diagonal elements are non-zero

A = [3, 7, 4, 9, 6]

def display():
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                print(A[i], end=" ")
            else:
                print(0, end=" ")
        print()


display()