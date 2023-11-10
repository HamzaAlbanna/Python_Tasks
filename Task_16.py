#c
def compareTriplets(a, b):
    Ales=0
    bobe=0
    for i in range(len(a)):
        if a[i]>b[i]:
            Ales+=1
        elif a[i]<b[i]:
            bobe+=1    
        
        
    return [Ales,bobe]      

  