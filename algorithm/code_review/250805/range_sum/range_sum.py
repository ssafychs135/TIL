import sys

sys.stdin = open('sample_input.txt')

T = int(input())

# 조건과 리스트 추출 시작
for tc in range(1, T+1):

    # 구간합 조건 case[0]: 원소 갯수 case[1]: 구간 크기
    case = list(map(int, input().split()))

    # 계산할 list 추출
    target_range: list = list(map(int, input().split()))

    # 최대 구간합을 저장할 변수 초기화
    max_range_sum = 0

    # 최소 구간합을 저장할 변수 초기화
    min_range_sum = 0

    # 남은 길이가 구간 크기보다 작으면 구간합 계산 불가능
    for i in range(0, case[0]-case[1]+1):

        # 구간합 초기화
        sum_of_range = 0
        
        # 구간 길이 만큼 원소를 더한다
        for j in range(case[1]):

            sum_of_range += target_range[i+j]

        # 구간합 최대 최소 갱신
        if max_range_sum < sum_of_range:
            max_range_sum = sum_of_range

        # 초기화를 0으로 해 주었기 때문에 최초 1회 0이여도 갱신 되도록 조건 추가
        if min_range_sum > sum_of_range or min_range_sum == 0:
            min_range_sum = sum_of_range

    # 결과 반환
    result_value = max_range_sum - min_range_sum
    print(f'#{tc} {result_value}')
