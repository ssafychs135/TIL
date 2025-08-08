import sys

sys.stdin = open('sample_input.txt')


T = int(input())

# 상단부터 시계방향으로 네 방향 참조를 도와줄 배열 작성
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for tc in range(1,1+T):

    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 최종 누적값 초기화
    result = 0

    # 행렬 순회 시작
    for i in range(N):
        for j in range(N):

            # 관심 좌표의 상하좌우를 추출한다
            for n in range(4):
                ni = i + di[n]
                nj = j + dj[n]

                # 조회하려는 인덱스가 행렬을 벗어나지 않는지 확인
                if 0 <= ni < N and 0 <= nj < N:
                    result += abs(matrix[ni][nj] - matrix[i][j])

    # 결과 출력
    print(f'#{tc} {result}')