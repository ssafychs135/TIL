import sys

sys.stdin = open('input.txt')


# Test case 갯수
T = int(input())

print(T)

# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
#
# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
#
# 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
#


# SWEA의 정답 출력 양식에 맟춰 case를 0부터가 아닌 1부터로 시작해준다
# Test Case 시작

for tc in range(1, T + 1):

    # list 초기화
    matrix = []

    # 리스트 요소 대신 인덱스를 사용하기 위해 input.txt 에서 주어진 list 길이
    N = int(input())
    print(N)
    for _ in range(N):

        row = list(map(int, input().split()))

        matrix.append(row)

        # list의 첫번째 값이 최대값이라 가정하고 초기화
        # max_v = tc[0]

        # list의 첫번째 값이 최솟값이라 가정하고 초기화
        # max_m = tc[0]

        # if tc[i] < tc[i+1]:
        #     max_v = tc[i+1]
        #
        # if tc[i] > tc[i + 1]:
        #     max_v = tc[i + 1]

    print(matrix)

# print(f'#{tc} {max_m-max_v}')
#
#
#
#
#
#
#
#
#
