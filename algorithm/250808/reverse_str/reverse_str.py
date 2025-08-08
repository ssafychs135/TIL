import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):

    txt = input()
    ############# 데이터 입력 #############

    # 뒤집은 문자열을 누적할 빈 문자열 준비
    # new_txt: str = ''

    for i in range(len(txt)):

        # 문자열 누적
        # new_txt += txt[len(txt)-i-1]
        # new_txt = txt[::-1]

        # reverse()사용
        new_txt = "".join(reversed(txt))
    print(f'#{tc} {new_txt}')

