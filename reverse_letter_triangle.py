
def print_pattern(n):
    
    char = "A"
    
    for i in range(1,n+1):
        for j in range(1,n+2-i):
            print(char,end=" ")
            
            char = chr(ord(char) + 1) # increments character
        char = "A" # resets to "A" for next row
        print() 
        
        
print_pattern(4)



"""
A B C D 
A B C 
A B 
A
"""


"""
ord() --> converts a character to its Unicode integer representation.

chr() --> converts a Unicode integer back to its corresponding character.
"""
