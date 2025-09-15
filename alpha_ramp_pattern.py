
def print_pattern(n):
    
    char = "A"
    
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(char,end=" ")
            
        char = chr(ord(char) + 1) # increments character
        print() 
        
        
print_pattern(4)


"""
A 
B B 
C C C 
D D D D
"""


"""

ord() --> converts a character to its Unicode integer representation.

chr() --> converts a Unicode integer back to its corresponding character.

"""
