
arr = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180]


def BinarySearch (list , num):
   
    ml=list 
    i =  len(ml)
    while (i > 0):
        if ml == []: return -1
        l = ml [0]
        m = ml [int(len(ml)/2)]
        h = ml [len(ml) -1]
        
        if num == m:
                
                return list.index(m)

        elif num > m :
                ml=list [list.index(m)+1: list.index(h)+1]
                i = i-len(ml)
                
            

        elif num < m :
                ml=list [list.index(l): list.index(m)]
                i = i-len(ml)
                
            

        
    return -1
            


print(BinarySearch(arr ,1))
