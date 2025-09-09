
def print_pattern(n):
  
    for i in range(1, n+1):           # Loop through rows from 1 to n
        for j in range(n, i-1, -1):   # Loop through columns from n down to i
            print(n-j+1, end=" ")     # Print increasing numbers starting from 1
        print()                        # Move to the next line after each row

print_pattern(5)                       # Call the function with n = 5
