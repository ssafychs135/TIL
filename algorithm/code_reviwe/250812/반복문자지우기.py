'''
※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.


문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데,
만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.

반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.
 

다음은 CAAABBA에서 반복문자를 지우는 경우의 예이다.
 

CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.

CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.

CAA 연속 문자 AA를 지운다.

C 1글자가 남았으므로 1을 리턴한다.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤ 50
 

다음 줄부터 테스트 케이스의 별로 길이가 1000이내인 문자열이 주어진다.

 

[출력]
 

#과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다.

'''

import sys

sys.stdin = open('반복문자지우기.txt')


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
    string = input()

    # 스택 공간 준비
    stack = Stack(len(string))
    
    # 문자열을 순회한다    
    for elm in string:
        
        # stack이 비어있다면 스택에 문자열 추가, 비교 위해 대기
        if stack.is_empty():
            stack.push(elm)
        else:
            # 스택의 top과 순회중인 문자열과 비교
            # 같으면 pop으로 지워준다
            if stack.peek() == elm:
                stack.pop()
            else:
                # 같지않으면 스택에 추가
                stack.push(elm)
    
    print(f'#{tc} {stack.top+1}') 