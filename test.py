import time


def sum_number(n):
    total = 0
    for i in range(n):
        total += i+1
    return total


def stickify(n, h, w, c):
    start = time.time()
    for i in range(n):
        for j in range(h):
            for k in range(w):
                for l in range(c):
                    sum_number(1000)

    end = time.time()
    print(f"{n}x{h}x{w}x{c} took {end - start} sec")


if __name__ == "__main__":
    stickify(1, 10, 1, 2000)
    stickify(1, 512, 2, 64) # NHWC
    stickify(1, 2, 64, 512) # NCHW
    stickify(1, 64, 512, 2) # NHWC
    # stickify(1, 64, 64, 1024)
