def printFun(num):
    if num < 1:
        return

    print("*" * num)
    printFun(num-1)
    print("*" * num)


if __name__=="__main__":
    printFun(3)