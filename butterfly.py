def print_pattern(n):

    # TOP HALF
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end="")
        
        for k in range(2*(n-i)+1,1,-1):
            print("_",end="")
        
        for l in range(1,i+1):
            print("*",end="")
        print() 
    
    # BOTTOM HALF
    for m in range(n-1,0,-1):
        for o in range(m):
            print("*",end="")
            
        for p in range(1,(6-2*m)+1,1):
            print("_",end="")
        
        for q in range(m):
            print("*",end="")
        
        print()
        
print_pattern(3)


#########################################
# ALTERNATE APPROACH
#########################################

def print_pattern(n):
    # Top half
    for i in range(1, n+1):
        print("*" * i + "_" * (2*(n-i)) + "*" * i)

    # Bottom half
    for i in range(n-1, 0, -1):
        print("*" * i + "_" * (2*(n-i)) + "*" * i)

print_pattern(3)

############## OUTPUT ############################

"""

*____*
**__**
******
**__**
*____*

"""
