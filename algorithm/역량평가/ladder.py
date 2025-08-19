import sys 

# from pprint import pprint as print

sys.stdin = open('ladder.txt')

di = [0, -1, 0]
dj = [-1, 0 ,1]


for tc in range(1, 11):

    input()

    ladder = [list(map(int, input().split())) for _ in range(100)]

    # ladder[99]는 사다리의 가장 마지막 행을 의미합니다.
    # 마지막 행에서 값이 2인 지점(도착점)을 찾아야 합니다.
    # 이 때, x좌표(열 인덱스)가 필요하므로 enumerate를 사용합니다.
    start_point = 0 # 도착점의 x좌표를 저장할 변수
    for x, val in enumerate(ladder[99]):
        # 마지막 행의 값을 하나씩 확인하면서
        if val == 2:
            # 값이 2이면, 해당 위치의 x좌표를 저장하고
            start_point = x # 도착점의 x좌표를 저장할 변수

            # 반복문을 멈춥니다.
            break
    
    # 시작점은 [99][start_point]이다
    r,c = 99, start_point
    while r > 0 :
        ladder [r][c] = 0
        
        # 왼쪽 확인
        if c - 1 >=0 and ladder[r][c-1] == 1:
            c -= 1
        # 오른쪽 확인
        elif c + 1 < 100 and ladder[r][c+1] == 1: 
            c += 1
        # 양쪽을 확인했는데도 길이 없으면 위로 올라간다
        else:
            r -=1



    print(f'#{tc} {c}')