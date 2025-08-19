'''
23569. 두 개의 탑

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

    # N개의 상자, M,K 각 탑의 높이
    N, M, K = map(int, input().split())

    numbers = list(map(int, input().split()))


    # 역순으로 정렬
    numbers.sort(reverse=1)

    tower_K = []
    sum_tower = 0

    # 한칸씩 넘어가면서 상자 추출
    # 추출 끝나고 남은 배열이 tower_M
    for x in range(K):
        tower_K.append(numbers.pop(x))
    
    # 각 타워의 비용을 구해 합해준다
    for i in range(K):
        sum_tower += tower_K[i]*(i+1)

    for j in range(M):
        sum_tower += numbers[j]*(j+1)
        


    print(f'#{tc} {sum_tower}')

