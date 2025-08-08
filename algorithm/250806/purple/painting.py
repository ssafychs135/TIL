import sys

sys.stdin = open('sample_input.txt')

# matrix 생성

matrix = list([0] * 10 for _ in range(10))

T = int(input())     # T : Test Case

for tc in range(1,1+T):

    # N: 내부 배열 갯수, 붓질을 몇번 하는지
    N = int(input())

    # 한 번에 붓질에서 칠하는 영역
    painting_area = [list(map(int, input().split())) for _ in range(N)]

    # 패인트가 칠해질 공간 초기화 10X10 행렬
    matrix = list([0] * 10 for _ in range(10))

    # 3이 넘으면 보라색이라 가정한다(1[빨강]과 2[파랑]의 합이 보라이기 때문)
    color_count = 0

    # 이하 반복에서 실제로 패인트를 칠해 봄
    for color in painting_area:

        for x in range(color[0], color[2]+1):
            for y in range(color[1], color[3]+1):

                # 0이면 무조건 칠한다
                # 1일경우 1이면 칠하지 않는다
                # 1일 경우 2면 칠한다
                # 2일 경우 2면 칠하지 않는다

                if matrix[x][y] is not color[4]:
                    matrix[x][y] += color[4]

                # 붓질 한 횟수가 2번이 넘었을때부터 붓질 이후에 해당 위치의 값이 3 이상이면 보라색으로 간주한다
                if matrix[x][y] == 3:
                    color_count += 1

    # 정답을 출력한다
    print(f'#{tc} {color_count}')
