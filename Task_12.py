#collections.Counter() | HackerRank | 

from collections import Counter as ctr

_ = input()
shoe_sizes_counter = ctr(map(int, input().split(' ')))
earning = 0

for _ in range(int(input())):
    size, price = tuple(map(int, input().split(' ')))
    if shoe_sizes_counter.get(size, 0):
        earning += price
        shoe_sizes_counter[size] -= 1

print(earning)