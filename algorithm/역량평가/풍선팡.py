import sys 
from pprint import pprint as print


sys.stdin = open('풍선팡.txt')

di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]


T = int(input())



for tc in range(1, 1+T):

    N, M = (map(int, input().split()))

    array = [list(map(int, input().split())) for _ in range(N)]

    max_pang = 0


    for i in range(N):
        for j in range(M):
            power = array[i][j]
            temp_pang = power

            for n in range(4):
                for d in range(1, power+1):
                    ni = i + di[n]*d
                    nj = j + dj[n]*d

                    if 0 <= ni < N and 0 <= nj < M:

                        temp_pang += array[ni][nj]

            if max_pang < temp_pang:
                max_pang = temp_pang 

    print(f'#{tc} {max_pang}')