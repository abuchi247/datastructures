visited = {
    "count": 0
}

fibs = {}
def fibonacci(n):
    visited["count"] = visited["count"]+1

    if n in fibs:
        return fibs[n]
    
    if n < 2:
        return n
    
    fibs[n] = fibonacci(n-1) + fibonacci(n-2)
    return fibs[n]

if __name__ == "__main__":
    print(fibonacci(10))
    print("Number of cals: ", visited["count"])