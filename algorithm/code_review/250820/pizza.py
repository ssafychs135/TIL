"""
N개의 피자를 동시에 구울 수 있는 화덕이 있다. 피자는 치즈가 모두 녹으면 화덕에서 꺼내며, 치즈의 양은 피자마다 다르다.

1번부터 M번까지 M개의 피자를 순서대로 화덕에 넣을 때, 치즈의 양에 따라 녹는 시간이 다르기 때문에 꺼내지는 순서는 바뀔 수 있다.

주어진 조건에 따라 피자를 구울 때, 화덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램을 작성하시오.

- 피자는 1번위치에서 넣거나 뺄 수 있다.
- 화덕 내부의 피자받침은 천천히 회전해서 1번에서 잠시 꺼내 치즈를 확인하고 다시 같은 자리에 넣을 수 있다.
- M개의 피자에 처음 뿌려진 치즈의 양이 주어지고, 화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다. 이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어든다.
- 치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그 자리에 남은 피자를 순서대로 넣는다.

[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄부터 테스트 케이스의 첫 줄에 화덕의 크기 N과 피자 개수 M이 주어지고, 다음 줄에 M개의 피자에 뿌려진 치즈의 양을 나타내는 Ci가 주어진다.

3<=N<=20, N<=M<=100, 1<=Ci<=20

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 번호를 출력한다.


#1 4
#2 8
#3 6

"""

import sys
from collections import deque

sys.stdin = open("pizza.txt")


T = int(input())

for tc in range(1, 1 + T):

    # N 화덕의 크기
    # M 피자 갯수
    N, M = list(map(int, input().split()))

    cheese = list(map(int, input().split()))

    # oven = deque(cheese[:N:])

    oven = deque()
    pizza_idx = 0

    # 최초 화덕 크기에 최대한 피자 넣음
    for i in range(N):
        pizza_idx += 1
        oven.append([cheese[i], pizza_idx])
    
    
    
    
    while len(oven) > 1:
        # print(oven)
        # 피자를 한판 꺼내봄
        pizza = oven.popleft()

        #치즈 확인
        now_cheese = pizza[0] // 2
        now_pizza_idx = pizza[1]
        
        
        # 치즈가 다 녹았으면
        if now_cheese == 0: 
            
            if pizza_idx < M:
                # 다음 피자 준비
                pizza_idx +=1   
                oven.appendleft([cheese[pizza_idx-1],pizza_idx])
    
        # 안녹았으면 다시 넣음
        else:
            oven.append([now_cheese,now_pizza_idx])
    

    


    print(f'#{tc} {oven.popleft()[1]}')
