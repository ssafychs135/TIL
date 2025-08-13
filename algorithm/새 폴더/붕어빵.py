import sys

sys.stdin = open('붕어빵.txt')

T = int(input())

for tc in range(1, 1+T):

    N, M ,K = map(int, input().split())
    customer = list(map(int, input().split()))
    
    # 붕어빵 제공 여부
    fish_flag = "Possible"
    
    # 손님들을 도착 시간순으로 정렬한다
    customer.sort()
    
    # 손님 받기 시작
    for p in range(N):
        
        # p 번째 손님이 왔을 때, 만들어진 붕어빵 수
        make = (customer[p]//M) * K

        # 만들어진 붕어빵이 손님 수 보다 적으면 실패!
        if make < p+1 :
            fish_flag = "Impossible"
            break
        
    print(f'#{tc} {fish_flag}')
