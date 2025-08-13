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
    
    

# 3개의 자료를 넣을 스택 준비
my_stack = Stack(3)

# 만들어진 스택에 실제로 값을 넣어본다
my_stack.push(1)
my_stack.push(False)
my_stack.push('C')

print(my_stack.push(9999))
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())