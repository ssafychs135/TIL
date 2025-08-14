import sys 

sys.stdin = open('행렬.txt')


T = int(input())

for tc in range(1, 2):
    
    N = int(input())
    
    warehouse = list(list(map(int, input().split())) for _ in range(N))

    # print(warehouse)
    
    # 델타로 풀어보자
    
    di = [0, -1, 0, 1]
    dj = [-1, 0, 1, 0]
    
    
    
    for i in range(N):
        for j in range(N):
            
            
            # 0이 아닌곳이기만 하면 된다
            if warehouse[i][j]:        
                
                for n in range(4):
                    position = 0
                    
                    for m in range(N):
                        ni = i + di[n] * m
                        nj = j + dj[n] * m
                        
                        if 0 <= ni <N and 0<= nj < N:
                            print(ni,nj)
                            if not warehouse[ni][nj]:
                                position+=1
                        # print(position)