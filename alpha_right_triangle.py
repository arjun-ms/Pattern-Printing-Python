def print_pattern(n):
    
    # outer loop for number of rows
    for i in range(1, n+1):
        
        # inner loop for characters in each row
        for j in range(1, i+1):
            
            # formula to calculate character:
            # start at 'A' + ( (n - 1) + col - row )
            # ensures shifting alphabets based on row
            char = chr(ord("A") + n - 1 + j - i)
            
            print(char, end=" ")  # print character with space
        
        print()  # move to next line
    
# call function
print_pattern(5)



"""
E 
D E 
C D E 
B C D E 
A B C D E
"""
