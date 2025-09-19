
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

#======================== EASY CODE ======================

def print_pattern(n):
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            # print star at borders
            if(i==1 or i==n or j==1 or j==n):
                print("*", end="")
            else:
                print(" ", end="")
        # move to next line after each row     
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


