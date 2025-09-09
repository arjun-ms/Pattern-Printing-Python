
def print_pattern(n):
    # for rows
    for i in range(n):
    
        # print stars
        for j in range(i+1):
            print("*", end=" ")
          
        # print spaces
        for k in range(n-i+1):
            print(" ", end=" ") 
            
        print()
    
    
print_pattern(5)

"""
* 
* * 
* * *
* * * *
* * * * *
"""
