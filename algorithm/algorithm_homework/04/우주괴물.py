'''

NxN개의 칸으로 나눠진 구역에 우주 괴물 한 마리가 침입했다. 괴물은 상하좌우로 광선을 발사하며, 벽에 막히지 않으면 광선은 계속 뻗어 나간다. 괴물의 광선이 닿지 않는 안전한 빈 칸의 수를 구하라.


그림1. 안전한 칸이 9칸인 경우의 예
 

 

[입력]

첫 줄에 테스트케이스 개수 T, 다음 줄부터 첫 줄에 N, 다음 줄부터 빈칸으로 구분된 N 칸의 정보가 N개의 줄에 걸쳐 제공된다. 각 칸은 0 (빈칸) 1(벽) 괴물(2) 중의 하나이다. (5<=N<=15)

 

[출력]

#과 테스트케이스 번호, 빈칸에 이어 답을 출력한다.

#1 9

'''

import sys 

sys.stdin  = open('우주괴물.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    space = list(list(map(int, input().split())) for _ in range(N))
    
    monster = []
    
    for i in range(N):
        
        for j in range(N):
            
            if space[i][j] == 2:
                monster = [i,j] 
                break
    
    di = [0,-1,0,1]
    dj = [-1,0,1,0]
    
    
    unsafe_area = 0
    
    for n in range(4):
        
        for m in range(N):
            ni = monster[0] + di[n]*m
            nj = monster[1] + dj[n]*m
            
            if 0<= ni <N and 0<= nj <N:
                
                if space[ni][nj] == 0:
                    unsafe_area += 1
                elif space[ni][nj] == 1:
                    break
                
                # if space[ni][nj] == 1:
                #     break
    
    block = 0
                
    for i in range(N):
                        
        for j in range(N):
             if space[i][j] == 1:
                 block +=1 
    
    
    print(f'#{tc} {N**2 - block -unsafe_area -1}')