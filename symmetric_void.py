# HARD

def print_pattern(n):
    
    
    for i in range(1,n+1):
    
        for j in range(1,n-i+2):
            print("*", end=" ")
            
        
        for k in range(0,2*i-2):
            print("_",end=" ")
        
        for l in range(n-i+1,0,-1):
            print("*",end=" ")
        
        print() 
      
 
    # 2nd half
    for z in range(1,n+1):   
        
        for m in range(1,z+1):
            print("*",end=" ")
        
        # 1st method   
        # Wrote the general form of a line: o = az+b
        # Plugged in the known points to find a and b
        # Checked the third point to confirm the equation is correct.
        # for o in range(-2*z+6,0,-1):
        #     print("_",end=" ")
        
        # 2nd method
        for o in range(2*(n-z)):
            print("_",end=" ")
            
        
        for p in range(0,z):
            print("*",end=" ")
        
        
        print()
    
        
print_pattern(3)


"""
* * * * * * 
* * _ _ * * 
* _ _ _ _ * 
* _ _ _ _ * 
* * _ _ * * 
* * * * * *
"""
