#function return  list(array) sum
def simpleArraySum(ar):

    sum=0
    for i in ar:
        sum+=i
    return sum    


ar = list(map(int, input().rstrip().split()))

result = simpleArraySum(ar)
print(result)
