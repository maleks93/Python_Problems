def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    
    size  = len(states)
    num = 0
    for i in range(size):
        num = num | states[i] << i
        
    num = ((num << 1) ^ (num >> 1))

    days -= 1
    print(num) 
    while(days > 0):
                    
                
        num = ((num << 1) ^ (num >> 1))
            
        days -= 1
    
    print(num)            
        
    for i in range(size):
        states[i] = 1 if (num & (1 << i)) > 0 else 0
        
        
    return states

print(cellCompete([1,1,1,0,1,1,1,1], 2))
