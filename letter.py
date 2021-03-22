def originalDigits(s: str) -> str:
        dict1={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
        s=[ch for ch in s]

        output=[]
        print(s)
        unique={0:"z",2:"w",4:"u",6:"x",8:"g"}
        nonunique={1:"n",3:"t",5:"v",7:"s",9:"i"}

        for x in s :
            # print(x)
            for ke,val in unique.items():
                # print(ke,val)
                if x==val :
                    output.append(ke)
                # else:
                #     ke+1
                #     val+1
            for key,valu in nonunique.items():
                print(ke,val)
                if x==valu :
                    output.append(key)


        print (output)       




print(originalDigits('fviefuro'))