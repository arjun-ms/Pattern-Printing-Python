
def print_pattern(n):
    # no of rows
    for i in range(n):
        # no of columns
        for j in range(1,i+2):
            print(j,end="")
        print()
    
print_pattern(5)

"""
1
12
123
1234
12345
"""
