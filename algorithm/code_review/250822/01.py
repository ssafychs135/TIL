import sys

sys.stdin = open('01.txt')

# 노드를 순회하기 위한 함수
def order(node):
    
    # 노드가 유효한 경우에만...
    if node !=0:
        # 전위순회이기 때문에 먼저 출력을 하고
        print(node, end = ' ')
        # 노드의 왼쪽 탐색 -> 오른쪽 탐색
        order(left[node])
        order(right[node])
    
# 정점의 갯수
V = int(input())

# 간선의 수
E  = V - 1

# 트리 데이터
tree = list(map(int, input().split()))


# 각 노드의 왼쪽,오른쪽 자식 정보를 저장할 리스트 생성
# root가 0번 node가 1부터기 때문에 V+1
left = [0] * (V + 1)
right = [0] * (V + 1)

# 간선 정보를 두개씩 짝지어 순회
for i in range(E):
    
    # 부모노드, 자식노드 2개씩 데이터가 들어오기 때문에
    parent, child = tree[i*2], tree[i*2+1]
    
    # 들어온 데이터를 이진트리 형식으로 그려봄
    # 데이터중 부모노드 정보를 기반으로 왼쪽부터 값이 채워져있는지 확인해본다
    # 채워져있지 않다면 왼쪽부터 채운다
    if left[parent] == 0:
        left[parent] = child
    
    # 왼쪽이 0이 아님 = 값이 채워져있음
    # 그렇다면 오른쪽에 채우자
    else:
        right[parent] = child
        

# 순회 시작        
order(1)