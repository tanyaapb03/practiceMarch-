def canJump(Lis) :
    position=0
    
    for x in range(len(Lis)):
        steps=Lis[position]
        print(steps)
        position=Lis[position+steps]
        print(position)
        print(Lis[len(Lis)-1])
        if position<Lis[len(Lis)-1]:
            continue
        else:
            break
    if position==Lis[len(Lis)-1]:
        return True
    if position>Lis[len(Lis)-1]:
        return False
canJump([3,2,1,0,4])   