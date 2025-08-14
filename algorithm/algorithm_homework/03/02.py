import sys
from pprint import pprint as print

sys.stdin = open('02.txt')


T = int(input())

for tc in range(1, T+1):
    
    # N 가로 , M 세로
    N, M = map(int, input().split()) 
    
    photo = [list(map(int, input().split())) for _ in range(N)]
    
    max_len = 0
    
    
    # 가로 순회
    for i in range(N):
        ml = 0
        for j in range(M):
            
            if photo[i][j]:
                ml +=1 
                
            else:
                if max_len < ml:
                    max_len = ml
        if max_len < ml:
                        max_len = ml
            
     # 세로 순회
    for i in range(N):
        ml = 0
        
        for j in range(M):
            
            if photo[j][i]:
                ml += 1
                
            else:
                if max_len < ml:
                    max_len = ml
        if max_len < ml:
                        max_len = ml
                    
    print(f'#{tc} {max_len}')