
def print_pattern(n):
        
    size = 2 * n - 1 # total rows and columns
    
    for i in range(1,size + 1):
        for j in range(1,size + 1):
            
            # distance from the nearest edge (1-based)
            dist = min(i - 1, j - 1, size - i, size - j)
            val = n - dist # Now we subtract that depth from n, This creates the shrinking square effect.
            print(val, end=" ")
        
        print() # NEXT ROW
    
        
print_pattern(3)


"""

3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3

"""
