
def print_pattern(n):
    # Outer loop → number of rows
    # i goes from 1 to n (inclusive)
    for i in range(1, n+1):
        # Inner loop → number of stars (*) per row
        # j goes from n down to i (inclusive)
        # This ensures the number of stars decreases by 1 each row
        for j in range(n, i-1, -1):
            print("*", end=" ")  # print a star followed by a space, stay on same line
        
        # Move to the next line after printing all stars in the current row
        print()

# Call the function with 6 rows
print_pattern(6)




"""

* * * * * *
* * * * * 
* * * * 
* * * 
* * 
* 

"""
