import sys 

sys.stdin = open('input.txt')

T = int(input())

# 테스트 케이스 시작
for tc in range(1, T+1):

    # 데이터 입력 시작
    num = int(input())
    num_list = list(map(input()))

    # 최대 반복 횟수
    num_count_max = 0

    # 임시 반복 횟수
    num_count_temp = 0

    # 순회 시작
    for i in range(10):

        # 순회하면서 1의 갯수를 센다
        if num_list[i] == 1:
            num_count_temp += 1

        else:
        # 1이 아닌걸 만나면 최대 카운트와 비교해서 업데이트 해 준다
            if num_count_max < num_count_temp: 
                num_count_max = num_count_temp
            num_count_temp = 0
    if num_count_max < num_count_temp:
        num_count_max = num_count_temp  

    print(f'#{tc} {num_count_max}')