

def print_pattern(n):
    
    for i in range(1,n+1):
        # to decide row start
        if i%2==0:
            start = 0
        else: 
            start = 1
            
        for j in range(1,i+1):
            print(start,end="")
            start = 1-start # flip between 0 and 1
            
        print() # move to next line
        
print_pattern(5)



"""
1
01
101
0101
10101
"""
