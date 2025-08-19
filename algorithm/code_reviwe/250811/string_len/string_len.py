import sys

sys.stdin = open("sample_input.txt")

T = int(input())

# 테스트 케이스 시작
for tc in range(1, 1+T):
    
    char_count = 0
    # 서로 비교할 문자열 배열
    string = list(input() for _ in range(2))
    
    
    counts = {}
    
    # 앞 문자열의 철자 하나씩 뒷 문자열과 비교해서 일치하면 카운트를 올린다
    for elm in string[0]:    
        
        # 현재 반복중인 철자의 출현 횟수
        counts[elm] = 0
        
        for inner in string[1]:
            
            if elm == inner:
                counts[elm] += 1

    
    # 요소 중 가장 많이 나온 철자의 반복 횟수를 담을 변수 초기화
    char_count = 0

    # 세어진 글자수의 딕셔너리에서 value 만 추출해서 비교한다
    for number in counts.values():
        if char_count < number:
            char_count = number
                    
    print(f'#{tc} {char_count}')