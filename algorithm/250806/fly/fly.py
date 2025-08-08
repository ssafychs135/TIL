import sys

sys.stdin = open('sample_input.txt')


T = int(input())

for tc in range(1,T+1):

    # N: 행렬의 크기
    # M: 파리채의 크기 결정
    N,M = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 파리채가 닿는 범위를 오른쪽 아래를 기준점으로 M*M 크기의 영역으로 간주
    # 파리채가 올려질수 있는 위치는
    # matrix[M-1][M-1]부터

    # 판별 시작 위치를 정하기 위한 초기값
    start = M - 1
    max_fly_kill = 0


    for i in range(N):
        for j in range(N):

            # 잡은 파리 수 초기화
            sum_fly_kill = 0

            # 파리채를 가져다 댄 기준점에서 파리채의 영역에 해당하는 좌표값들을 누적해본다
            for r in range(i-M+1, i+1):
                for c in range(j - M + 1, j + 1):

                    # 파리채의 영역이 행렬 안에 있을 경우에만 누적한다
                    if 0 <= r < N and 0 <= c < N:
                        sum_fly_kill += matrix[r][c]

                # 누적한 값과 역대 최대값과 비교해서 누적값이 더 크면 갱신해준다
                if max_fly_kill < sum_fly_kill:
                    max_fly_kill = sum_fly_kill

    # 결과를 출력한다
    print(f'#{tc} {max_fly_kill}')