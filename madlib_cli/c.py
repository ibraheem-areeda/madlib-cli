
arr = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180]


def BinarySearch (list , num):
    if num > list [len(list)-1]:
        return -1
    elif num < list [0]:
          return -1
    ml=list 
    i =  len(ml)
    while (i > 0):
        if ml == []: return -1
        l = ml [0]
        m = ml [int(len(ml)/2)]
        h = ml [len(ml) -1]
        print(l,m,h)
        if num == m:
                print(1111111,len(ml),i,(i > 1),"m=",m,"l=",l,"h=",h)
                return list.index(m)

        elif num > m :
                ml=list [list.index(m)+1: list.index(h)+1]
                i = i-len(ml)
                print(22222,len(ml),i,(i > 1),ml,"m=",m,"l=",l,"h=",h)
            

        elif num < m :
                ml=list [list.index(l): list.index(m)]
                i = i-len(ml)
                print(333333,len(ml),i,(i > 1),ml,"m=",m,"l=",l,"h=",h)
            

        
    return -1
            


print(BinarySearch(arr ,100))
