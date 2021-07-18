def perm_sol1(s, k):
    """
    Time complexity: O(N!)
    Space complexity: O(N)
    """
    print(f"First A={A}")
    if k == len(s):
        print(res)
    else:
        for i in range(len(s)):
            print(f"A={A}")
            if A[i] == 0:
                print(f"before: i={i}, k={k}, A={A}, res={res}")
                res[k] = s[i]
                A[i] = 1
                print(f"after: i={i}, k={k}, A={A}, res={res}")
                perm_sol1(s, k+1)
                A[i] = 0


def swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp


def perm_sol2(arr, l, h):
    if l == h:
        print(arr)
    else:
        for i in range(l, h+1):
            swap(arr, l, i)
            perm_sol2(arr, l+1, h)
            swap(arr, l, i)


s = ["A", "B", "C"]
A = [0]*len(s)
res = [""]*len(s)

# perm_sol1(s, 0)
perm_sol2(s, 0, 2)