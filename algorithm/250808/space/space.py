import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):


    tcn, counts = list(map(str, input().split()))

    numbers = list(input().split())

    key_number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    sorted_numbers = ''

    for idx in range(10):
        num_count = 0
        for num in numbers:

            if num == key_number[idx]:
                num_count += 1

        # print(key_number[idx],num_count)
        temp = (key_number[idx]+" ") * num_count
        # print(temp)
        sorted_numbers += temp


    print(f'{tcn}, {sorted_numbers}')
