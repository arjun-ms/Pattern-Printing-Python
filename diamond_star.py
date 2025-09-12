def print_pattern(n):
    # ----------------------
    # UPPER PYRAMID (1 to n)
    # ----------------------
    for i in range(n):
        # Print leading spaces
        # Formula = (n - i - 1)
        for j in range(n-i-1, 0, -1):
            print(" ", end="")

        # Print stars
        # Formula = (2*i + 1), grows by 2 each row
        for k in range(2*i+1):
            print("*", end="")

        # Newline after each row
        print()

    # ----------------------
    # LOWER PYRAMID (n down to 1)
    # ----------------------
    for i in range(n, -1, -1):
        # Print leading spaces
        # Formula = (n - i)
        for j in range(n-i, 0, -1):
            print(" ", end="")

        # Print stars
        # Formula = (2*i - 1), shrinks by 2 each row
        for k in range(2*i-1, 0, -1):
            print("*", end="")

        # Newline after each row
        print()


# Driver code
print_pattern(3)
