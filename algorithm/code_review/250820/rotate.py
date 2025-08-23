import sys

from collections import deque

sys.stdin = open('rotate.txt')


T = int(input())

for tc in range(1, T+1):
    
    N, M = list(map(int, input().split()))
    
    numbers = list(map(int, input().split()))
    
    
    my_que = deque(numbers)
    
    my_que.rotate(-M)
    
    print(f'#{tc} {my_que.popleft()}')