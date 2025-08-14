import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):

    N = int(input())

    row = list(map(int, input().split()))

    # print(f'초기 배열: {row}')

    # 반복이 한번 될때마다 뒤에서부터 정렬이 된다
    # 왜? 한 칸 앞까지의 구간들을 서로 모두 비교해보기 때문!

    # # 버블정렬 시작
    # for i in range(N-1, 0, -1):
    #
    #     # 여기서 맨 마지막 자리는 제외하고 순회 된다
    #     # 왜? 순회의 마지막에서 앞의 원소들중 가장 큰 것과 비교 될 것이기 때문
    #     # 더 크면 자리 유지, 작으면 앞으로 이동
    #
    #     for j in range(i):
    #
    #         # 배열 앞의 값이 더 크면 자리를 바꿔준다
    #         if row[j] > row[j+1]:
    #             row[j], row[j + 1] = row[j + 1], row[j]


    # 선택 정렬 시작



    # 다른 원소와 비교하기때문에 마지막 한 칸에 대한 직접적인 비교는 필요 없다
    for i in range(N-1):
        # 최소값의 인덱스를 첫번째로 가정해보자
        min_idx = i

        # i+1 로 비교중인 첫번째 원소는 빼고 가져온다
        for j in range(i+1, N):
            if row[min_idx] > row[j]:
                min_idx = j
        row[i], row[min_idx] = row[min_idx], row[i]


    print(f'#{tc} {" ".join(map(str, row))}')
