import sys

sys.stdin = open('sample_input.txt')

T = 10


for tc in range(1, T + 1):
    start_point = int(input())


    ladder = [list(map(int, input().split())) for _ in range(100)]


    # 사다리 게임은 위로 올라가는 경우, 대각선으로 움직이지 않는다
    di = [0, 1, 0]
    dj = [1,0, -1]


    # 사다리 이동 원칙 아래로 내려감> 좌우블록 확인> 좌우 블록을 향해 끝까지이동 > 더 이상 갈 수 없다면 다시 아래로


    # 출발 가능 좌표
    start = []
    for idx in range(100):

        if ladder[idx] == 1:
            start.append(idx)

    for point in start:

        ladder[0][point]


        for n in dj:

           if ladder[0][point+n] == 1:

            # while ladder[0][point + 1] == 0:
            #     pass
            # while ladder[0][point - 1] == 0:
            #     pass






    # 나의 시작 좌표는 무조건 ladder[0][n] 이다
    # 도착좌표는 ladder[99][n] = 2인 곳이다

    # 좌우 확인 후 아래로 가야한다
    pass
