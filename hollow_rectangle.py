
def print_pattern(n):
    
    
    for i in range(1,n+1):
        
        # First and last row -> print all stars
        if i==1 or i==n:
            for j in range(1,n+1):
                print("*",end=" ")
        
        # Middle rows -> stars only at first and last column       
        else:
            for k in range(1,n+1):
                if k==1 or k==n:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
        
        print()
    
        
print_pattern(6)


"""

* * * * * * 
*         * 
*         * 
*         * 
*         * 
* * * * * *

"""
