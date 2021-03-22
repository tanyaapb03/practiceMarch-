#exclusive time of function 
def exclusive(n,logs):
    


    # logs=log.split(",")
    
    steps=[0]*n
    stack=[]
    time_correction=[0]
    for log in logs:
        id,action, time=log.split(":")
        print (id,action, time)
        if action == "start":
            stack.append((id,int(time)))
            time_correction.append(0)
            print (time_correction)
        else:
            print(steps,time,stack,time_correction)
            steps[int(id)] += int(time) - stack[-1][1] + 1 - time_correction.pop()
            print(steps,time,stack,time_correction)
            time_correction[-1] += int(time) - stack[-1][1] + 1
            stack.pop()
    return steps
            

        
        
        # if output.keys!= None:
        #     output.keys=id
        # if sos=="start":

        #     steps=+steps
        # if sos=="end ":
        #     output.keys=counter.append(steps)

   








   
print(exclusive(2,["0:start:0","1:start:2","1:end:5","0:end:6"]))



