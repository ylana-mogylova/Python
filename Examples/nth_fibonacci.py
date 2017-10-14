"""
Write a function that returns the nth number in the fibonacci’s sequence
"""


def fibonum(n):   # Give the nth fibonacci number
    x = [0, 1]
    for i in range(2, n):
        x.append(x[i-2]+x[i-1])

    return x[n-1]


if __name__ == "__main__":
    nth = 9
    print("%s fibonacci number is %s" % (nth, fibonum(nth)))
