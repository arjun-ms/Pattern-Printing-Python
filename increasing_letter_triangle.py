
def print_pattern(n):
    
    char = "A"
    
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(char,end=" ")
            
            char = chr(ord(char) + 1) # increments character
        char = "A" # resets to "A" for next row
        print() 
        
print_pattern(4)


"""

ord() --> converts a character to its Unicode integer representation.

chr() --> converts a Unicode integer back to its corresponding character.

"""

"""

A 
A B 
A B C 
A B C D

"""

# MORE CLEANER VERSION

def print_pattern(n):
    for i in range(1, n+1):
        for j in range(i):
            print(chr(ord("A") + j), end=" ")
        print()

print_pattern(6)
  
