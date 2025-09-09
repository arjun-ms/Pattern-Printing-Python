def print_pattern(n):
    # for rows
    for i in range(n):
        # for columns
        for j in range(n):
            print("*", end=" ")
        print() # for breaking into next line
    
    
print_pattern(5)


"""
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
"""
