def counting_sort(input_arr, k):

    # 정렬된 배열을 준비해준다
    sort_row: list = [0] * len(input_arr)

    # 데이터 내의 등장 횟수를 카운트해서 담을 배열
    # 데이터 내 최대 값 혹은 입력받은 k값(요소 중 최대값) 기준으로 배열을 만들어준다
    counts: list = [0] * k  # counts = [0, 0, 0, 0, 0]
    print(counts)
    # 데이터의 요소를 counts 배열의 index로 사용해 해당 위치의 값에 1씩 추가한다
    for num in input_arr:  # counts = [1, 3, 1, 1, 2]

        counts[num] += 1

    # counts의 누적으로 배열을 바꿔준다
    # index 0에 대해서는 누적합이 의미 없기 때문에 연산에서 제외해준다
    for i in range(1, k):  # counts = [1, 4, 5, 6, 8]

        counts[i] += counts[i - 1]

    # 재배열 시작

    # 우선 원본 배열(row)로 부터 값을 하나씩 가져온다
    for num in input_arr:
        print(num)
        # 가져온 값을 index로 counts 배열에서 조회한다
        # index는 0부터 시작하므로 -1 해준다
        sort_row_index = counts[num] - 1

        # 구한 인덱스 위치에서부터 채운다
        sort_row[sort_row_index] = num

        # 자릿수를 하나 채웠기때문에 -1 을 해서 조정
        counts[num] -= 1

    # 정렬된 list를 반환한다
    return sort_row    # return [0, 1, 1, 1, 2, 3, 4, 4]


arr = [0, 4, 1, 3, 1, 2, 4, 1]
print('정렬 결과:', counting_sort(arr, 5))    # [0, 1, 1, 1, 2, 3, 4, 4]