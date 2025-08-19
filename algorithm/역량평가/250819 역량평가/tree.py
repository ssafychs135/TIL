import sys

# "tree.txt" 파일에서 입력을 읽어오도록 설정합니다.
sys.stdin = open("tree.txt")

def solve_without_binary_search():
    """
    하나의 테스트 케이스를 해결하는 함수 (순차 탐색 방식).
    """
    # 나무의 개수 N을 입력받습니다.
    N = int(input())
    # 각 나무의 초기 높이를 리스트로 입력받습니다.
    woods = list(map(int, input().split()))

    # 나무가 하나거나 없으면 성장이 필요 없으므로 0일을 반환합니다.
    if N <= 1:
        return 0

    # 가장 키가 큰 나무의 높이를 찾습니다.
    max_height = 0
    for w in woods:
        if w > max_height:
            max_height = w
    
    # 필요한 +1 성장(홀수 날)과 +2 성장(짝수 날)의 총 횟수를 계산합니다.
    total_ones = 0
    total_twos = 0
    for w in woods:
        # 현재 나무와 가장 큰 나무의 높이 차이를 계산합니다.
        diff = max_height - w
        # 높이 차이를 2로 나눈 몫만큼 +2 성장이 필요합니다.
        total_twos += diff // 2
        # 높이 차이를 2로 나눈 나머지만큼 +1 성장이 필요합니다.
        total_ones += diff % 2

    # 모든 나무의 키가 이미 같아서 성장시킬 필요가 없으면 0일을 반환합니다.
    if total_ones == 0 and total_twos == 0:
        return 0

    # 날짜를 0부터 시작하여 1씩 증가시키며 확인합니다.
    day = 0
    while True:
        day += 1
        
        # 'day'일 동안 가능한 짝수 날과 홀수 날의 수
        even_days = day // 2
        odd_days = (day + 1) // 2

        # 짝수 날로 채우지 못한 +2 성장의 수
        unfulfilled_twos = 0
        if total_twos > even_days:
            unfulfilled_twos = total_twos - even_days
        
        # 최종적으로 필요한 홀수 날의 총 수
        needed_odd_days = total_ones + unfulfilled_twos * 2
        
        # 필요한 홀수 날의 수가 주어진 홀수 날의 수보다 작거나 같으면,
        # 현재 'day'가 최소 날짜입니다.
        if needed_odd_days <= odd_days:
            return day # 조건을 만족하는 첫 날짜를 찾았으므로 반환하고 종료합니다.

# 가장 첫 줄에 주어진 테스트 케이스의 총 수를 읽어옵니다.
T_str = input()
# 파일 끝에 빈 줄이 있는 경우 등 예외 상황을 처리합니다.
if T_str:
    T = int(T_str)
    # 각 테스트 케이스를 순회하며 문제를 풉니다.
    for tc in range(1, 1 + T):
        result = solve_without_binary_search()
        # 형식에 맞게 결과를 출력합니다.
        print(f"#{tc} {result}")
