import sys

sys.stdin = open('괄호검사.txt')


# Stack 클래스 정의
class Stack:
    
    # 길이가 고정된 스택 자료형이 초기화 되는 곳
    def __init__(self, size):
        
        self.size = size #스택 생성 시 주어진 길이
        self.capacity = [None] * size # 길이 고정
        self.top = -1 # 최초에는 어떠한 자료 입력이 없기 때문에 비어있다
    
    # 스택이 비어있음을 확인하는 함수
    def is_empty(self):
        return self.top == -1
    
    
    # 스택의 가장 위(top)에서 원소를 하나 반환하고 제거함
    def pop(self):
        
        # 우선 비어있는지 확인한다
        if self.is_empty():
            return "stack Underflow"
        
        # 반환하기 위해 가장 위의 값을 저장한다
        item = self.capacity[self.top]
        
        # 일반적인 pop의 행동을 따라하기 위해 가장 윗 값을 비워준다
        self.capacity[self.top] = None
        
        # 원소를 하나 지웠으므로 스택 포인터도 하나 감소시킨다
        # !주의! 1씩 빼는거니까 빼는 숫자에 - 를 붙이지 않는다
        self.top -= 1
        
        # 저장해둔 값을 반환한다
        return item 
    
    
    # 입력받은 자료를 스택의 가장 위에 위치시킨다
    def push(self, item):
        
        # 내부 동작은 List와 동일하기 때문에 List 보다 top이 작은 경우에만 추가 가능하기 때문에 먼저 확인해준다
        # 이미 가득 차 있는 상태면 오버플로우를 반환한다
        if self.top >= self.size - 1:
            return "Stack Overflow"
        # 가득 차 있지 않다면 탑을 증가시키고 증가된 탑 위치에 입력받은 자료를 넣어준다
        self.top += 1
        self.capacity[self.top] = item
    
    
    # 스택의 가장 윗 값을 반환한다, 단 비어있다면 비어있다고 알린다
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.capacity[self.top]

T = int(input())

for tc in range(1, T+1):
    parentheses = input()
    
    # 괄호의 갯수보단 스택이 적을 예정이기 때문에 스택의 크기를 괄호 갯수로 지정하였다
    stack = Stack(len(parentheses))
    
    # 괄호가 올바르게 쓰였는지 저장하는 변수
    failure = 1
    
    
    # 괄호들을 순회한다
    for elm in parentheses:
        
        # 만약 ( 를 만나면 스텍에 저장해준다
        if elm == '(':
            stack.push(elm)
        
        # ) 를 만나면... 
        else:
                # 우선 스택이 비어있는지 확인해본다
                # 비어있다면 잘못된 괄호 사용이다, 바로 반복문을 빠져나가도 된다
                if stack.is_empty():
                    failure = -1
                    break
                # 비어있지 않다면 ( 괄호를 하나 스택에서 제거해준다
                else:
                    stack.pop()
    
    
    # 최종적으로 괄호가 남았는지 확인해준다
    if not stack.is_empty():
        failure = -1
        
    print(f'#{tc} {failure}')
    