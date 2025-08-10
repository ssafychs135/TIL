
import sys

sys.stdin = open("sample_input.txt")

T = int(input())

# 상 하 좌 우 확인확인
ni = [0, -1, 0, 1]
nj = [-1, 0, 1, 0]

# 대각선 확인
na = [-1, -1, 1, 1]
nb = [-1, 1, 1, -1]


for tc in range(1, 1+T):

    N , M = list(map(int, input().split()))

    spray = [list(map(int , input().split())) for _ in range(N)]


    # 내 위치에서 M 범위 만큼을 확인하는걸 도와줄 델타 배열 정의
    # 가로세로, 대각선 두 버전이 필요하다
  
    fly_kill = 0
    
    # 순회 시작
    for i in range(N):
        for j in range(N):


            fly_kill_a = 0
            fly_kill_b = 0
            
          
            # 델타 행렬에 대한 연산: 기준점 (i,j)에 대한 상하좌우 대각
            for r in range(4):
                # 분사 범위 M 만큼 떨어진곳까지의 합
                # 스프레이 분사 범위에 대해 반복
                for p in range(1, M):    
                    # 직각방향
                    di = i + ni[r]*p
                    dj = j + nj[r]*p

                    # 대각방향
                    bi = i + na[r]*p
                    bj = j + nb[r]*p

                    if 0 <= di < N and 0 <= dj < N: 
                        fly_kill_a += spray[di][dj]
                        # print(f'직각 {di},{dj} = {spray[di][dj]}')
                    
                    if 0 <= bi < N and 0 <= bj < N: 
                        fly_kill_b += spray[bi][bj]
                        # print(f'대각 {bi},{bj} = {spray[bi][bj]}')

                    if fly_kill_a > fly_kill_b:

                        fly_kill_temp = fly_kill_a
                    else:
                        fly_kill_temp = fly_kill_b


            if fly_kill < fly_kill_temp +spray[i][j]:

                fly_kill = fly_kill_temp + spray[i][j]


    print(fly_kill)



    
