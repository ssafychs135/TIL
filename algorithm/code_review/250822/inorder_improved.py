
import sys

# 'inorder.txt' 파일로부터 입력을 읽어옵니다.
sys.stdin = open('inorder.txt')

# 중위 순회(in-order traversal)를 재귀가 아닌 반복문과 스택을 이용하여 구현합니다.
# 이렇게 하면 재귀 깊이 제한에 걸리지 않습니다.
def inorder_traversal(start_node):
    """
    스택을 이용한 중위 순회 함수

    Args:
        start_node (int): 순회를 시작할 노드(일반적으로 루트 노드인 1)

    Returns:
        str: 중위 순회 결과로 만들어진 문자열
    """
    # 순회 결과를 저장할 문자열
    result_word = ""
    # 방문할 노드들을 임시로 저장할 스택
    stack = []
    # 현재 처리 중인 노드
    current_node = start_node

    # current_node가 유효하거나(0이 아니거나) 스택에 아직 노드가 남아있는 동안 계속 반복
    while current_node != 0 or stack:
        
        # 1. 왼쪽 자식 노드로 계속 이동하며 스택에 추가
        #    - 현재 노드가 유효하면(0이 아니면) 계속 왼쪽으로 파고듭니다.
        #    - 이동하는 경로에 있는 모든 노드는 스택에 저장됩니다.
        while current_node != 0:
            stack.append(current_node)
            current_node = left[current_node]
        
        # 2. 스택에서 노드를 꺼내 방문 (처리)
        #    - 왼쪽 끝까지 다다르면(current_node가 0이 되면), 스택에서 가장 마지막에 추가된 노드를 꺼냅니다.
        #    - 이 노드가 중위 순회에서 방문해야 할 다음 노드입니다.
        current_node = stack.pop()
        
        # 3. 꺼낸 노드의 문자를 결과에 추가
        #    - word 리스트에서 해당 노드 번호에 맞는 문자를 찾아 결과 문자열에 더합니다.
        result_word += word[current_node]
        
        # 4. 오른쪽 자식 노드로 이동
        #    - 현재 노드의 방문이 끝났으므로, 이제 오른쪽 자식 노드를 방문할 차례입니다.
        #    - current_node를 오른쪽 자식으로 설정하고, 다시 1번 과정부터 반복합니다.
        current_node = right[current_node]
        
    return result_word

# 총 10개의 테스트 케이스가 주어집니다.
T = 10

for tc in range(1, 1 + T):
    # 정점의 총 수 N을 입력받습니다.
    N = int(input())
    
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

    # 루트 노드(1)부터 중위 순회를 시작하고 결과를 출력합니다.
    result = inorder_traversal(1)
    print(f'#{tc} {result}')
