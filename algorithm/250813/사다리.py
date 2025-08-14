import sys

sys.stdin = open('사다리.txt')

# 사다리 게임이기때문에 위로 올라가는 경우는 없다

di = [0, 1, 0]
dj = [-1, 0, 1]


for tc in range(1, 11):
    
    input()
    
    ladder = list(list(map(int, input().split())) for _ in range(100))
    
    
    # 도착 판별: y 좌표가 99인 경우 도착이다
    move_count_min = float("inf")
    print(move_count_min)
    
    
    # 1인 곳만 반복을 돌리기 위해 조건을 건다
    for start in range(100):
        move_count = 0
        # 사다리게임 시작 ladder[0][start]
        if ladder[0][start]:
            # 사다리게임 원칙에 따라 좌우 확인 후 없으면 아래로 보낸다, 언제까지? 벽이 나올때까지
            
            # 최초 시작점기록, 좌표 이동시마다 누적
            x = 0
            y = start
            # x가 99이면 정지: ?
            
            
            
           # 시작점에서 주변을 확인한다
            while x < 99:
                # 왼쪽이나 오른쪽에 길이 있는 경우
                # 왼쪽
                if 0 < y and ladder[x][y-1] ==1:
                    while 0 < y and ladder[x][y-1] ==1: 
                        move_count += 1
                        y+=-1 
                elif y+1 <99  and ladder[x][y+1] == 1:
                    while y < 99 and ladder[x][y+1] ==1:
                        move_count += 1
                        y+=1 
                x += 1
                move_count+=1
                
            if move_count_min > move_count:
                move_count_min =move_count    

    
    print(move_count_min)           
                    
    
    