
def print_pattern(n):
    
    for i in range(1,n+1):
        
        for j in range(1,i+1):
            print(j,end=" ")
        
        # for spaces somehow connecct the n and i with k
        for k in range(2*(n-i)-1,-1,-1):
            print("_",end=" ")
            
        for l in range(i,0,-1):
            print(l,end=" ")

        print() # move to next line
        
print_pattern(4)





"""
1 _ _ _ _ _ _ 1 
1 2 _ _ _ _ 2 1 
1 2 3 _ _ 3 2 1 
1 2 3 4 4 3 2 1
"""
