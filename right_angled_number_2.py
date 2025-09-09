
def print_pattern(n):
    # for rows
    for i in range(n):
        # for columns
        for j in range(1,i+2):
            print(i+1,end="")  # print row number
        print() # for next line
    
print_pattern(5)

"""

1
22
333
4444
55555

"""
