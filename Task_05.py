#Runner up score
arr = map(int, input().split())
lst = list(set(arr))
lst.sort()
print(lst[-2])  