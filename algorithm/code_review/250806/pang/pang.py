import sys

sys.stdin = open('sample_input.txt')

T = int(input())     # T : Test Case


# 상단부터 시계방향으로 네 방향 참조를 도와줄 배열 작성
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for tc in range(1,1+T):

    # N: row 의 갯수
    # M: 내부 배열 길이
    N, M = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 순회 시작
    count = 0
    for i in range(N):

        for j in range(M):

            # 시작점의 꽃가루 양
            power = matrix[i][j]

            # 날린 꽃가루를 누적할 임시 값, 자기 자신도 터지므로 본인의 값으로 초기화
            temp = power

            # power 만큼 좌표 이동 시도
            for x in range(1,power+1):

                # 기준점에서 1칸~power칸 까지 떨어진만큼 시계방향으로 조회해본다
                for n in range(4):
                    ni = i + di[n]*x
                    nj = j + dj[n]*x

                    # 조회된 좌표가 실제 좌표평면 위라면 그 위치의 값을 임시값에 누적시킨다
                    if 0 <= ni < N and 0 <= nj < M:
                        temp += matrix[ni][nj]


            # 누적값이 기존값보다 크면 갱신
            if count < temp:
                count = temp

    print(f"#{tc} {count}")
