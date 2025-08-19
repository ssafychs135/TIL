import sys

'''
#1 12

#2 13

#3 7
'''

sys.stdin = open('main.txt')

T = int(input())

for tc in range(1, 1+T):

    N = int(input())

    portal = list(map(int, input().split()))

    # 포탈 이용 횟수
    count = 0

    # 내가 지금 위치한 방
    now = 0

    # 해당 방 방문횟수를 기록할 리스트 생성
    room_count = [0] * N

    # 첫번째 방은 시작과 동시에 방문한다
    room_count[0] = 1

    # now가 5보다 커지면 마지막에 왔다고 볼 수 있다
    while now  < N-1:
        count += 1
        # 각 방에 들어가본다
        # 방에 도착했을 때 방문했던 방이라면 바로 다음방으로
        # 아니라먄 portal[now] 로 이동

        # 방문한적 있는 곳이라면
        if room_count[now] == 1:
            # 다음 방으로 이동하는 포탈 사용
            now += 1
        # 방문 한 적 없는 곳이라면
        else:
            # 해당 방을 방문하였음으로 업데이트
            room_count[now] = 1
            # 방문 한 방에 적혀있는 위치로 현위치 변경, 인덱스와 방 번호간에 1 차이가 있어서 -1 해준다
            now = portal[now]-1
            
    print(f'#{tc} {count}')