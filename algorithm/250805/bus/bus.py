import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):

    case: list = list(map(int, input().split()))

    bus_move = case[0]   # 1회 충전시 버스 이동 가능 거리
    route_length = case[1]    # 버스 노선 길이
    charger = case[2]    # 노선에 설치된 버스 충전기 갯수
    bus_stop: list   # 버스 정거장을 표현할 list 준비

    # 충전기 위치정보를 가지고 있는 list
    charge_point: list = list(map(int, input().split()))

    for i in range(len(charge_point)-1):

        # 버스 충전 횟수 초기화
        charge_count = 0

        # 충전기 있는 구간의 차가 버스 이동가능거리 보다 큰 경우엔 모든 남은 연산을 버리고 0을 출력한다
        if charge_point[i+1] - charge_point[i] > bus_move:
            pass
        else:
            # 버스 노선 길이 만큼의 list를 준비한다
            bus_stop = [0] * (route_length + 1)

            # 버스 충전기 위치를 버스루트에 표시한다
            for point in charge_point:

                bus_stop[point] = 1

            # 출발점에서 남은 주행거리
            remain_dist = bus_move

            # 버스 운행 시작
            for d in range(route_length):
                # 충전기 도착
                for j in range(0, len(charge_point) - 1):

                    # 충전소 도착
                    if d == charge_point[j]:

                        # 다음 충전소까지의 거리 확인
                        next_spot = charge_point[j+1] - charge_point[j]

                        # 다음 충전소까지 거리와 비교해보기
                        # 남은 주행거리 = 충전횟수 * 1회 충전 이동 거리 - 현위치
                        remain_dist = (charge_count * bus_move) - d

                        if remain_dist < next_spot:
                            charge_count += 1

    print(f'#{tc} {charge_count}')



