'''
#1 29
#2 63
#3 95
#4 447
#5 226521
'''

import sys

sys.stdin = open('두개의탑.txt')

T = int(input())

for tc in range(1, T+1):

    N, M, K = map(int, input().split())

    numbers = list(map(int, input().split()))

    numbers.sort()

    numbers = numbers[::-1]

    a = []

    sum_tower = 0

    for x in range(K):
        a.append(numbers.pop(x))
    
    for i in range(K):
        sum_tower += a[i]*(i+1)

    for j in range(M):
        sum_tower += numbers[j]*(j+1)
        


    print(sum_tower)

