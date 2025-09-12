def print_pattern(n):
    # Outer loop -> controls the number of rows
    # Starts from n and goes down to 1 (decreasing rows)
    for i in range(n,-1,-1):
        
        
        # for printing leading spaces
        # Number of spaces = (n - i)
        # As i decreases, spaces increase
        for j in range(n-i,0,-1):
            print(" ",end="")
            
        # for printing stars
        # Number of stars = (2*i - 1), always odd
        # This creates the shrinking pyramid effect
        for k in range(2*i-1,0,-1):
            print("*",end="")
        
        # Move to the next line
        print()
    
            

print_pattern(3)


"""

*****
 ***
  *

"""
