import sys

sys.stdin = open('sample_input.txt')



T = int(input())

for tc in range(1, T + 1):

    # N 행렬의 가로,세로의 길이
    # M 찾고자하는 회문의 길이
    N, M = list(map(int, input().split()))

    string = [list(input()) for _ in range(N)]

    # 가로 순회시작
    for i in range(N):
        row = ''
        for j in range(N):
            row += string[i][j]

        # 만들어진 row 에 대해 M 칸씩 잘라보면서 회문이 있는지 확인
        for idx in range(M):

            # idx를 시작점으로 해서 M 칸만큼 잘라야 한다
            if idx + M > N:
                break
            else:
                # 회문 확인을위해 제시된 조건만큼 문자열 편집
                new_row = row[idx:idx + M]

                if new_row == new_row[::-1]:
                    print(f"#{tc} {new_row}")

    # 세로 순회
    for i in range(N):
        cols = ''
        for j in range(N):
            cols += string[j][i]
        # 이제 만들어진 cols에 대해 문자열을 M 칸씩 끊어가며 회문인지 확인해본다
        new_cols = ''

        for idx in range(M):

            # idx를 시작점으로 해서 M 칸만큼 잘라야 한다
            if idx + M > N:
                break
            else:
                # 회문 확인을위해 제시된 조건만큼 문자열 편집
                new_cols = cols[idx:idx + M]

                if new_cols == new_cols[::-1]:
                     print(f"#{tc} {new_cols}")




