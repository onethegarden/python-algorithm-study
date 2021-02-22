# 환형 큐(Circular Queues)



### 큐의 활용

- 자료를 생성하는 작업과 그 자료를 이용하는 작업이 비동기적으로 일어나는 경우
- Producer가 쌓고, Consumer가 사용
- 컴퓨터 시스템(운영체제)에서 많이 사용

<br/><br/>

### 환형 큐 

- 정해진 개수의 저장 공간을 빙 돌려가며 이용
- 큐가 가득 차면 더 이상 원소를 넣을 수 없음 -> 큐 원소를 기억해야 함.
- ```isFull``` : 연산 추가 큐에 원소가 꽉 차 있는지를 판단



<br/><br/>

### 배열로 구현한 환형 큐

- 정해진 길이의 list를 미리 확보해 둠

- front(제일 먼저 꺼낼 값) 와 rear(맨 마지막 값)을 적절히 이용하여 구현

  ```python
  class CircularQueue:
  	def __init__(self, n):
  		self.maxCount = n #인자로 주어진 최대 큐 길이 설정
  		self.data = [None]*n
  		self.count = 0
  		self.front = -1
  		self.rear = -1
          
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
      
      def peek(self): #큐의 맨 앞 원소 리턴
          if self.isEmpty():
              raise IndexError('Queue empty')
          return self.data[(self.front + 1) % self.maxCount]
  ```

  

- 최대 큐의 길이를 이해해야 한다. 


<br/><br/>

**Enqueue 예시**

- 길이가 5인 큐가 있고 각각 1, 2, 3, 4, 5가 들어가 있고 dequeue를 한 번 수행했다고 가정하자.

  | 값     | 1(유효하지 않은 값) | 2    | 3    | 4    | 5    |
  | ------ | ------------------- | ---- | ---- | ---- | ---- |
  | 인덱스 | 0                   | 1    | 2    | 3    | 4    |

  현재 ```front = 0```, ```rear = 4```이다. 

  이제 ```enqueue(6)``` 을 수행하려고 하는데 rear의 값은 4이고, 인덱스 0의 위치에 값을 넣어야 하므로 rear의 값은 0 이 나와야 한다. 

  그러므로 배열의 길이로 현재 위치를 나누어야 하는데, 배열의 시작은 0이므로 +1을 해준다.

  ```python
  (self.rear + 1) % self.maxCount
  ```

- 그림을 그려가며 이해하면 조금 더 쉽다. 
