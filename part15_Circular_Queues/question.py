'''
Python 의 내장 데이터형인 리스트 (list) 를 이용하여 환형 큐의 추상적 자료 구조를 구현한 클래스 CircularQueue 를 완성하세요.

[참고] 함수 solution() 은 이 클래스의 구현과는 관계 없는 것이지만, 문제가 올바르게 동작하는 데 필요해서 넣어 둔 것이니 무시해도 좋습니다.
또한, 실행 을 눌렀을 때 예시 테스트 케이스를 통과한다고 출력되는 것은 아무런 의미가 없습니다.

'''
class CircularQueue:

    def __init__(self, n):
        self.maxCount = n
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1


    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.maxCount

    def enqueue(self, x):
        if self.isFull():
            raise IndexError('Queue full')
        self.rear = (self.rear + 1) % self.maxCount
        self.data[self.rear] = x
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        self.front = (self.front + 1) % self.maxCount
        x = self.data[self.front] 

        self.count -= 1
        return x

    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[(self.front + 1) % self.maxCount]


def solution(x):
    return 0


queue = CircularQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue.data)
print(f'뺀 값 : {queue.dequeue()}')
print(f'뺀 값 : {queue.dequeue()}')
queue.enqueue(6)
print(queue.data)
print(queue.peek())
