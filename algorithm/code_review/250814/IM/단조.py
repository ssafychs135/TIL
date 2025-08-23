import sys 

sys.stdin = open('단조.txt')


T = int(input())

for tc in range(1, 1+T):
    
    
    N = int(input())
    
    numbers = list(map(int, input().split()))
    
    # print(numbers)
    
    result = -1
    
    for i in range(N-1):
        
        # 자릿수를 추출하기 위한 값
        for j in range(i+1,N):
            value = numbers[i] * numbers[j]
        
        # 단조 증가 중 가장 큰 것을 찾기 위해 비교할 대상
            value_temp = value
        
            if value_temp < 10:
                if result < value_temp:
                    result = value_temp
                continue    
            
            # 가장 오른쪽 자릿수를 저장
            prev_digit = value_temp % 10
            # 다음 자릿수를 추출하기 위한 준비
            value_temp //= 10
            
            while value_temp > 0:
                
                # 그 다음 자릿수를 저장
                current_digit = value_temp % 10
                
                # 단조증가를 이루고 있는지 확인해본다
                if current_digit > prev_digit:
                    break
                
                
                # 다음 비교를 위해 준비한다
                prev_digit = current_digit
                value_temp //= 10
        
            else:
                if result < value:
                    result = value
                

    print(f'#{tc} {result}')
        
        