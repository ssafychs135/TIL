import sys 


# 후위표현식으로 바꾸는 함수
def infix_to_postfix(expression : str) -> str:
    # 각 연산자의 우선순위를 딕셔너리로 정의
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    # 연산자를 임시로 저장한 스택 정의
    stack = []
    # 최종 후위 표기법 결과를 담을 리스트 정의
    result = []

    # 입력된 중위 표기법 식을 토큰 단위로 순회
    for token in expression:
        # 1. 피연산자(숫자, 문자)일 경우
        if token.isalnum():
            # 바로 결과 리스트에 추가
            result.append(token)
        
        # 2. 여는 괄호 '('인 경우
        elif token == '(':
            # 우선순위와 상관없이 무조건 스택에 push
            stack.append(token)

        # 3. 닫는 괄호 ')'인 경우
        elif token == ')':
            # 스택 top이 여는 괄호가 될때까지 모든 연산자를 pop하여 결과에 추가
            # (스택이 비어있지 않고, top이 여는 괄호가 아닌 동안 반복)
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            # 반복이 끝나면 스택 top은 '('이므로, 이를 pop하여 버림
            stack.pop()

        # 4. 연산자인 경우
        else:
            # 스택 top의 연산자 우선순위(isp)와 현재 연산자 우선순위(icp) 비교
            # 스택이 비어있지 않고, top이 여는 괄호가 아니며,
            # isp가 icp보다 높거나 같으면 계속 pop
            while (
                stack
                and stack[-1] != '('
                and precedence.get(stack[-1], 0) >= precedence.get(token, 0)
            ):
                result.append(stack.pop())
            # 위 조건을 만족하지 않으면 (자기(token)보다 우선순위가 낮은 연산자를 만나면)
            # 현재 연산자(token)를 스택에 push
            stack.append(token)

    
    # 5. 모든 토큰 처리가 끝난 후 스택에 남아있는 연산자 처리
    # stack이 빌 때 까지 pop
    while stack:
        # 스택의 모든 연산자를 pop하여 결과에 추가
        result.append(stack.pop())
    
    # 6. 결과 리스트에 모든 요소를 하나의 문자열로 변환
    return ''.join(result)

sys.stdin = open('01.txt')


T = int(input())

for tc in range(1, 1+T):
    
    
    calc = input()
    
    
    print(f'{tc} {infix_to_postfix(calc)}')