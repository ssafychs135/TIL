import sys 

sys.stdin = open('회문검사.txt')


T = int(input())

for tc in range(1, 1+T):


    string = input()


    is_hwemoon = 1

    length = len(string)

    for i in range(length//2):

        if string[i] != string[::-1][i]:
            is_hwemoon = 0

    print(f'#{tc} {is_hwemoon}')