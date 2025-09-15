
def print_pattern(n):
    
    char = "A"
    
    for i in range(1,n+1):
        
        # printing spaces
        for j in range(n-i,-1,-1):
            print("_",end="")
            
        # printing left alphabets
        for k in range(1,i+1):
            print(char, end="")
            char = chr(ord(char)+1) #  move to next alphabet
        
        # step back once to avoid repeating the center
        char = chr(ord(char)-1)

        # printing right alphabets (descending order)     
        for l in range(i-1):
            char = chr(ord(char)-1) # move back to prev alphabet
            print(char, end="")
            
            
        # printing spaces
        for m in range(n-i,-1,-1):
            print("_",end="")
         
        char = "A"      # resets to "A" for next row
        print()         # go to next row
        
print_pattern(4)


"""
____A____
___ABA___
__ABCBA__
_ABCDCBA_
"""
