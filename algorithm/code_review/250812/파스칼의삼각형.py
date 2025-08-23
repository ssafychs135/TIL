
import sys

sys.stdin = open('파스칼의삼각형.txt')

T = int(input())

for tc in range(1, T+1):
    stack = int(input())

    # 스택 공간 준비
    # stack = Stack(len(string))
    
    my_list = [[1]]
    
    for num in range(2,stack+1):
        temp_list = [0] * num
        for n in range(num):
            
            
            
            my_list[num-1]
        