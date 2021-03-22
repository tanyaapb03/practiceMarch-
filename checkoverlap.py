def checkOverlap(radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # check distance of rectangle coordinate to center of circle and use condition to check if it is more or less than radius
        
    A=(x1,y2)
    B=(x1,y1)
    C=(x2,y1)
    D=(x2,y2)
        
    disA=[(x1-x_center),(y2-y_center)]
    # if distance-r ==0 
    if (disA[0]-radius) == 0 or (disA[1]-radius) == 0:
        return True 
        
    
        
    disB=[(x1-x_center),(y1-y_center)]
    if (disB[0]-radius) == 0 or (disB[1]-radius) == 0:
        return True 
    disC=[(x2-x_center),(y1-y_center)]
    if (disC[0]-radius) == 0 or (disC[1]-radius) == 0:
        return True 
    disD=[(x2-x_center),(y2-y_center)]
    if (disD[0]-radius) == 0 or (disD[1]-radius) == 0:
        return True 
    else:
        return False 
        
    print(disA,disB, disC, disD)
print(checkOverlap(radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3))   