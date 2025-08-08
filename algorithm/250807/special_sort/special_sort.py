import sys

sys.stdin = open('sample_input.txt')




'''

보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.

N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
 

10 1 9 2 8 3 7 4 6 5
 

주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오



3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26


#1 10 1 9 2 8 3 7 4 6 5
#2 89 8 85 11 67 16 60 28 49 39
#3 98 3 97 9 88 17 75 18 71 21	 




'''

T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    row = list(map(int, input().split()))

    sorted_row = [0] * 10
    # 선택정렬 시작
    for i in range(N-1):

        # 최소값의 idx가 i라 가정
        min_idx = i

        for j in range(i+1, N):

            if row[min_idx] > row[j]:
                min_idx = j

        # 실제 값 이동
        row[i], row[min_idx] = row[min_idx], row[i]



    # 가장 왼쪽 가장 오른쪽 수를 준비한다
    left, right = 0, N-1

    # 재배치된 배열에 채워나갈 idx
    sorted_row_idx = 0

    # 왼쪽부터 다가오는 수와 오른쪽부터 다가오는 수가 교차하지 않게
    while left <= right and sorted_row_idx < 10:
        sorted_row[sorted_row_idx] = row[right]

        # 다음 숫자를 넣기 위해 준비
        sorted_row_idx += 1
        right -= 1


        # 여전히 left와 right 가 교차하지 않았는지 확인
        if left <= right:
            sorted_row[sorted_row_idx] = row[left]

            # 다음 숫자를 넣기 위해 준비
            sorted_row_idx += 1
            left += 1

    print(f'#{tc} {" ".join(map(str, sorted_row))}')







































