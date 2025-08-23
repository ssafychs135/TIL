import sys

sys.stdin = open('sample_input.txt')


'''

코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.

짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.

예를 들어 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 중간 페이지 c= int((l+r)/2)로 계산한다.

찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.

A는 300, B는 50 쪽을 찾아야 하는 경우, 다음처럼 중간 페이지를 기준으로 왼쪽 또는 오른 쪽 영역의 중간 페이지를 다시 찾아가면 된다.
 

 

A

B

첫 번째 탐색

l=1, r=400, c=200

l=1, r=400, c=200

두 번째 탐색

l=200, r=400, c=300

l=1, r=200, c=100

세 번째 탐색

 

l=1, r=100, c=50


책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때, 이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하시오. 비긴 경우는 0을 출력한다.

#1 A
#2 0
#3 A


'''


T = int(input())

for tc in range(1, T + 1):

    # 전체쪽수, a가 찾을 페이지 , b 가 찾을 페이지
    page, *target_page = list(map(int, input().split()))

    count = [0, 0]

    winner = ''

    # 2명이 게임을 한다 반복문 시작
    for i in range(2):

        # 이진탐색 시작
        # 새 플레이어가 게임을 시작할때마다 초기화 됨
        start = 1
        end = page
        middle = 0


        while start <= end:

            # 책을 펼쳐본다
            count[i] += 1
            middle = (start + end) // 2 # 이진탐색의 기준이 될 탐색 기준점을 찾는다

            if middle == target_page[i]: # 페이지를 찾은 경우
                break
            elif middle < target_page[i]: # 목표 페이지가 기준값 오른쪽에 있는 경우
                start = middle  # 기준값보다 작은 곳들은 버린다
            else:
                end = middle

    if count[0] < count[1]:
        winner = 'A'
    elif count[0] == count[1]:
        winner = 0
    else:
        winner = 'B'

    print(f'#{tc} {winner}')