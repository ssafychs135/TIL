class Queue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.rear == self.capacity - 1

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("큐가 가득 찼습니다.")
        self.rear += 1
        self.items[self.rear]  = item

    def dequeue(self):
        if self.is_empty():
            raise IndexError('큐가 비었습니다.')
        self.front += 1
        item = self.items[self.front]
        self.items[self.front] = None
        
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError('큐가 비었습니다.')
        # 큐의 맨 앞을 반환
        return self.items[self.front+1]
        

    # 큐의 길이
    def get_size(self):
        if self.is_empty():
            raise IndexError('큐가 비었습니다.')
        return self.rear - self.front


# --- 기본 동작 예시 코드 ---
print("--- 1. 기본 동작 확인 ---")
queue = Queue(5)  # 용량이 5인 큐 생성

# 1. Enqueue (데이터 삽입)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(f"큐의 현재 크기: {queue.get_size()}")  # 3
print(f"큐의 맨 앞 데이터 확인(peek): {queue.peek()}")  # 10
print(f"큐 내부 리스트 상태: {queue.items}\n")  # [10, 20, 30, None, None]

# 2. Dequeue (데이터 추출)
# 가장 먼저 넣은 10이 가장 먼저 나옴 (FIFO)
print(f"Dequeue: {queue.dequeue()}")  # 10
print(f"큐의 현재 크기: {queue.get_size()}")  # 2
print(f"큐의 맨 앞 데이터 확인(peek): {queue.peek()}")  # 20
print(f"큐 내부 리스트 상태: {queue.items}")  # [None, 20, 30, None, None]
