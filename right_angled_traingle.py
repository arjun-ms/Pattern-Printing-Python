
def print_pattern(n):
 # outer loop → rows
    for i in range(n):
        # inner loop → columns (stars)
        for j in range(i + 1):
            print("*", end=" ")
        # move to next line after each row
        print()
    
    
print_pattern(5)

"""
* 
* * 
* * *
* * * *
* * * * *
"""
