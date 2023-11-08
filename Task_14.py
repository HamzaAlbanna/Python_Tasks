#set -> average function 
def average(array):
    sum=0
    counter=0
    for i in set(array):
        sum+=i
        counter+=1 
    return sum/counter   
    # your code goes here
#test
l=[1,3,4,5]
print(average(l))