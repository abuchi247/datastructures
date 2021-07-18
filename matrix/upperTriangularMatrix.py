# Array where non-zero elements in the row index <= col index are non zero

A = []

def display(A):
    for i in range(5):
        for j in range(5):
            if i <= j:
                print(A[i+j], end=" ")
            else:
                print(0, end=" ")
        print()


def populate(A):
    for i in range(5):
        for j in range(5):
            if i <= j:
                A.append(i+1)


populate(A)
print(len(A))
display(A)