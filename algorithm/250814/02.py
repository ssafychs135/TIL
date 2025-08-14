import sys

def evaluate_postfix(expression : str):
    """
    후위 표기법으로 표현된 수식을 계산하여 결과를 반환하는 함수.

    Args:
        expression (str): 후위 표기법으로 작성된 문자열 (예: "53+2*")

    Returns:
        int or float: 수식의 최종 계산 결과
    """
    
    # 피연산자를 임시로 저장할 stack
    stack = []
    
    # 후위 표기법 수식을 왼쪽부터 순회
    for token in expression:
        # 1. 토큰이 숫자인 경우
        if token.isdigit():    
            # 스택에 push
            stack.append(int(token))
        # 2. 토큰이 연산자인 경우
        elif token == '.':
            # 모든 연산이 끝난 후, 스택에 마지막으로 남은 값 하나가 최종 결과가 된다
            return stack.pop()
        else:
            # 스택에서 피연산자 2개를 pop
            # (중요) 먼저 꺼낸 것이 연산의 오른쪽에 위치함
            if len(stack) >= 2 :
                right = stack.pop() # 두번째 피연산자
                left = stack.pop()  # 첫번째 피연산자
            else:
                return 'error'
            # 토큰에 따라 적절한 연산 수행
            
            if token == "+":
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == "*":
                stack.append( left * right)
            elif token == '/':
                if right== 0:
                    return 'error'
                stack.append( left / right)
            elif token == '^':
                stack.append( left ** right)
            else:
                # 정의되지 않는 연산자가 들어올 경우 처리
                return 'error'

    


sys.stdin = open('02.txt')


T = int(input())

for tc in range(1, 1+T):
    
    
    calc = input().split()
    
    print(f'#{tc} {evaluate_postfix(calc)}')