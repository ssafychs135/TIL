import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    # 소인수 준비
    soinsu = [2, 3, 5, 7, 11]

    # 소인수분해 출력물 누적할 곳 준비
    bunhea: str = ''

    for elm in soinsu:
        count = 0

        # 소인수분해는 나머지가 있으면 안되기 때문에 나머지가 없을 때 까지 나눠준다
        while N % elm == 0:

            # 나머지 없이 나눠질 때만 나눈 횟수에 누적한다
            count += 1

            # 나누기에 성공했으므로 실제 값도 나눠준다
            N //= elm

        # 얼마나 나눴는지 결과에 적어준다
        bunhea += f' {count}'

    # 출력한다
    print(f'#{tc}{bunhea}')