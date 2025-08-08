import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):

    txt = input()
    ############# 데이터 입력 #############


    # 뒤집어진 문자열과 비교하는 법
    # print(f"#{tc} {int(txt == txt[::-1])}")

    # 양 끝의 문자열을 비교해서 회문검사 하는 법

    for i in range(len(txt)//2):

        is_reversed = True

        if txt[i] != txt[len(txt)-i -1]:
            is_reversed = False
            break


    print(f'#{tc} {int(is_reversed)}')