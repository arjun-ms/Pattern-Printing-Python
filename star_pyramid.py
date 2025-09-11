
def print_pattern(n):
    
    # no of rows
    for i in range(1,n+1):
        
        # no of cols (somehow connect them to rows)
        
        # whitespaces (shrinks as row increases)
        for j in range(n-i,0,-1):
            print(" ",end="")
            
        # Left half of the pyramid (same as of i)
        """
            start = 0 (default)
            stop = i (the number you gave)
            step = 1 (default)
        """
        for k in range(i):
            print("*",end="")
        
        # Right half of the pyramid 
        # (i-1 stars, to avoid duplicating the center)
        for l in range(i-1):
            print("*",end="")  
        
        # whitespaces  
            # NO NEED TO PRINT THE WHITESPACES
        
        print() # Move to the NEXT ROW
            

print_pattern(4)


"""

   *
  ***
 *****
*******

"""
