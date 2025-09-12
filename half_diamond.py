def print_pattern(n):
    for i in range(1, 2*n):
        if i <= n:
            stars = i          # increasing part
        else:
            stars = 2*n - i    # decreasing part

        for j in range(stars):
            print('*', end="")

        print()


print_pattern(3)

"""

*
**
***
**
*

"""


# ANOTHER APPROACH

def print_pattern(n):
    # Upper half
    for i in range(1, n+1):
        for j in range(i):
            print("*", end="")
        print()

    # Lower half
    for i in range(n-1, 0, -1):
        for j in range(i):
            print("*", end="")
        print()


print_pattern(5)
