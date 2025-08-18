import sys 
from pprint import pprint as print


sys.stdin = open('파리퇴치.txt')


T = int(input())



for tc in range(1, 1+T):

    N, M = (map(int, input().split()))

    array = [list(map(int, input().split()) )for _ in range(N)]

    max_kill = 0


    for i in range(N):
        for j in range(N):
            temp_kill = 0
            array[i][j]

            for r in range(M):
                for c in range(M):

                    if i+r < N and j+c < N:
                        temp_kill += array[i+r][j+c]


            if max_kill < temp_kill:
                max_kill = temp_kill 

    print(f'#{tc} {max_kill}')