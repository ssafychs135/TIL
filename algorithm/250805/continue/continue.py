import sys

sys.stdin = open('sample_input.txt')

T = int(input())

# 조건과 리스트 추출 시작
for tc in range(1, T+1):

    # 데이터 입력 받음
    n = int(input())
    row = list(map(int, input()))

    # 마지막에 0을 추가하는것은 결과에 영향을 미치지 않는다
    row.append(0)

    # 연속횟수를 배열에 담아둔다
    continue_count = []

    # 연속횟수 초기화
    temp_count = 0

    # 연속된게 나오나 확인해본다
    for elm in row:

        # 연속이면 카운트를 늘려준다
        if elm == 1:
            temp_count += 1

        else:
            # 여태까지 누적된 연속횟수를 배열에 담고 연속 횟수를 초기화한다
            continue_count.append(temp_count)
            temp_count = 0

    # 출력한다
    print(f'#{tc} {max(continue_count)}')