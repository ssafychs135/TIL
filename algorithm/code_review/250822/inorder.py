'''
주어진 트리를 in-order 형식으로 순회해 각 노드를 읽으면 특정 단어를 알 수 있다.
 


 
위 트리를 in-order 형식으로 순회할 경우 SOFTWARE 라는 단어를 읽을 수 있다.
주어진 트리를 in-order 형식으로 순회했을때 나오는 단어를 출력하라.

[제약 사항]

트리는 완전 이진 트리 형식으로 주어지며, 노드당 하나의 문자만 저장할 수 있다.

노드는 아래 그림과 같은 순서로 주어진다.
 


[입력]

총 10개의 테스트 케이스가 주어진다. (총 테스트 케이스의 개수는 입력으로 주어지지 않는다)

각 테스트 케이스의 첫 줄에는 트리가 갖는 정점의 총 수 N(1≤N≤100)이 주어진다. 그 다음 N줄에 걸쳐 각각의 정점 정보가 주어진다.

정점 정보는 해당 정점의 문자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점 번호 순서로 주어진다.

정점 번호는 1부터 N까지의 정수로 구분된다. 정점 번호를 매기는 규칙은 위 와 같으며, 루트 정점의 번호는 항상 1이다.

위의 예시에서,  알파벳 ‘F’가 2번 정점에 해당하고 두 자식이 각각 알파벳 ‘O’인 4번 정점과 알파벳 ‘T’인 5번 정점이므로 “2 F 4 5”로 주어진다.
알파벳 S는 8번 정점에 해당하므로 “8 S” 로 주어진다.


[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.

#1 SOFTWARE
#2 COMPUTER_SCIENCE_AND_ENGINEERING
#3 SOFWARE_ALGORITHM_AND_DATA_STRUCT
#4 DEPTH_FIRST_SEARCH_AND_BREATH_FIRST_SEARCH
#5 WELCOME_TO_ALGORITHM_PROBLEM_SOLVING
#6 ARRAY_STRING_STACK_QUEUE_TREE_GRAPH
#7 HE_WHO_WOULD_HAVE_THE_KERNEL_MUST_CRACK_THE_SHELL
#8 THE_PRESENT_IS_THE_PRESENT_MOMENT
#9 IN_ORDER_PRE_ORDER_POST_ORDER_TRACE
#10 TECHNOLOGY_TRAINING_INSTITUTE


'''


import sys


sys.stdin = open('inorder.txt')


def order(node):
    global word, char

    if node != 0:
        order(left[node])
        char += word[node]
        order(right[node])
   
    return char

# 총 10개의 테스트 케이스가 주어집니다.
T = 10

for tc in range(1, 1 + T):
    # 정점의 총 수 N을 입력받습니다.
    N = int(input())
    char = ''
    # 각 노드의 왼쪽 자식, 오른쪽 자식, 그리고 문자를 저장할 리스트를 초기화합니다.
    # 인덱스를 1부터 N까지 사용하기 위해 크기를 N+1로 설정합니다.
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    word = [''] * (N + 1) # 노드 번호를 인덱스로 바로 사용하기 위해 리스트로 변경

    # N개의 줄에 걸쳐 정점 정보를 입력받습니다.
    for _ in range(N):
        # 입력값을 공백 기준으로 나눕니다. 예: "1 W 2 3" -> ['1', 'W', '2', '3']
        value = list(input().split())
        
        # 노드 번호와 문자를 추출합니다.
        node_idx = int(value[0])
        node_char = value[1]
        
        # word 리스트에 노드 번호를 인덱스로 하여 문자를 저장합니다.
        word[node_idx] = node_char
        
        # 왼쪽 자식 정보가 있으면 left 리스트에 추가합니다.
        if len(value) >= 3:
            left[node_idx] = int(value[2])
        
        # 오른쪽 자식 정보가 있으면 right 리스트에 추가합니다.
        if len(value) == 4:
            right[node_idx] = int(value[3])
        
 

    # print(order(1))
    print(f'#{tc} {order(1)}')
    
    
