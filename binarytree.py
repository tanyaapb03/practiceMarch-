#Queries on a Permutation With Key


def processQueries(queries, m):
    p=list(range(1,m+1,1))
    print(p)
    # i=0
    output=[]
    for i in range(len(queries)):
        
        position = p.index(queries[i])
        output.append(position)
        
        p.insert(0, p.pop(position))
        print(p)


        print (output)
       
processQueries([3,1,2,1],5)
 