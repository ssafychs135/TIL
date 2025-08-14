'''

N X N 크기의 판이 있다. 판의 각 칸에는 돌이 있거나 없을 수 있다. 돌이 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정하는 프로그램을 작성하라.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(5 ≤ N ≤ 20)이 주어진다.

다음 N개의 줄의 각 줄에는 길이 N인 문자열이 주어진다. 각 문자는 ‘o’또는 ‘.’으로, ‘o’는 돌이 있는 칸을 의미하고, ‘.’는 돌이 없는 칸을 의미한다.

  
[출력]

각 테스트 케이스 마다 돌이 다섯 개 이상 연속한 부분이 있으면 “YES”를, 아니면 “NO”를 출력한다.


#1 YES
#2 YES
#3 YES
#4 NO	 


'''
# from pprint import pprint as print


import sys

sys.stdin = open('오목판정.txt')

T = int(input())

for tc in range(1,T+1):
    
    N = int(input())
    
    stones = list(list(map(str, input())) for _ in range(N)) 
    
    
    # 나로부터 5칸 확인
    # 가로 세로 대각
    
    di = [0,-1,-1,-1,0,1,1,1]
    dj = [-1,-1,0,1,1,1,0,-1]
    
    
    omok = 'NO'
    # 
    # for i in range(N):
    #     count = 0
    #     for j in range(N):
    #         if stones[i][j] == 'o':
    #             count += 1 
    #     if count >= 5:
    #         omok = 'YES'          
    
    # for i in range(N):
    #     count = 0
    #     for j in range(N):
    #         if stones[j][i] == 'o':
    #             count += 1 
    #     if count >= 5:
    #         omok = 'YES'          
            
    # count = 0
    # for i in range(N):
        
    #     if stones[i][i] == 'o':
    #             count += 1 
    #     if count >= 5:
    #         omok = 'YES'    
            
    # count = 0
    # for i in range(N):
    #     # print(i, N-1-i)
    #     if stones[N-1-i][i] == 'o':
    #             count += 1 
    #             # print(count)
    #     if count >= 5:
    #         omok = 'YES'
    
    
    for i in range(N):
        
        for j in range(N):
            
            for n in range(8):
                
                count = 0
                
                for m in range(5):
                    ni = i + di[n] * m
                    nj = j + dj[n] * m
                    
                    # print(i,j,ni,nj)
                    
                    if 0<= ni <N and 0<= nj <N:
                        #print('돌 더하는 중')
                        if stones[ni][nj] == 'o':
                            count += 1
                            #print(count)
                    
                if count >= 5:
                    omok = "YES"
                
    
    

        
    
    
    
    print(f'#{tc} {omok}')