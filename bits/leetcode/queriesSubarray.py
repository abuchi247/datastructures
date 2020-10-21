def query(arr, l, r):
    pref = [] # to store the XOR of all entries in the array

    # pref[i] = A0^A1^A2^....^Ai

    for entry in arr:
        if len(pref) == 0:
            pref.append(entry)
        else:
            last = pref[-1]
            pref.append(last ^ entry)

    if l < 0:
        return None # out of bound
    if r >= len(arr):
        return None # out of bound

    if l == 0:
        return pref[r]

    return pref[r] ^ pref[l-1]

if __name__ == "__main__":
    print(query([1,3,4,8], 0, 1))
    print(query([1,3,4,8], 1, 2))
    print(query([1,3,4,8], 0, 3))
    print(query([1,3,4,8], 3, 3))