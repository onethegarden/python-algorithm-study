# 큐(Queues)



> 자료(data element)를 보관할 수 있는 (선현) 구조
>
> 단, 넣을 때는 한 쪽 끝에서 밀어넣어야하고 (enqueue 연산)
>
> 꺼낼 때에는 반대 쪽에서 뽑아 꺼내야 함. (dequeue 연산)
>
> 선입선출(FIFO - First-In-First-out)



<br/><br/>

### 1. 큐의 동작

```python
Q = Queue()
Q.enqueue(A) #위에서 아래로 데이터를 밀어넣음
Q.enqueue(b)

|B|
|A|

r1 = Q.dequeue() #r1 = A

|B|
| |

r2 = Q.dequeue() #r2 = B

| |
| |
```



<br/><br/>

### 2. 큐의 추상적 자료구조 구현

- **연산의 정의** 

  	1. ```size()``` - 현재 큐에 들어 있는 데이터 원소의 수를 구함
  	2. ```isEmpty()``` - 현재 큐가 비어 있는지를 판단
  	3. ```enqueue(x)``` - 데이터 원소 ```x```를 큐에 추가
  	4. ```dequeue() ``` - 큐의 맨 앞에 저장된 원소를  제거/반환
  	5. ```peek()``` - 큐의 맨 앞에 저장된 데이터 원소를 반환 (제거하지 않음)

  

- **구현**

1. 배열(array)을 이용하여 구현

   ```python
   class ArrayQueue:
       def __init__(self):
           self.data = [] #빈 큐를 초기화
        
   	def size(self): #큐의 크기를 리턴
           return len(self.data)
       
       def isEmpty(self): #큐가 비어있는지 판단
           return self.size() == 0
       
       def enqueue(self, item): #데이터 원소를 추가
           self.data.append(item)
           
   	def dequeue(self): #데이터 원소를 삭제(리턴)
           return self.data.pop(0) #stack과 다른 경우, 0을 삭제했을 시 나머지 원소들이 앞으로 당겨짐
       def peek(self): #큐의 맨 앞 원소 반환
           return self.data[0]
   ```

   - 배열로 구현한 큐의 연산 복잡도

   | 연산      | 복잡도 |
   | --------- | ------ |
   | size()    | O(1)   |
   | isEmpty() | O(1)   |
   | enqueue() | O(1)   |
   | dequeue() | O(n)   |
   | peek()    | O(1)   |

   ```dequeue() ``` 의 경우 0번째 원소를 꺼낼 때 앞에서부터 당겨오기 때문에 n만큼의 연산시간이 소요된다.

   스택의 경우 제일 마지막 원소를 꺼내기 때문에 부담이 없는데 큐의 경우에는 이 연산을 실행하려면 시간이 소요된다.

   <br/><br/>

2. 연결리스트(linked list) 를 이용하여 구현 (양방향)

   ```python
   class LinkedListQueue:
   
       def __init__(self):
           self.data = DoublyLinkedList() #DoublyLinkedList는 이전에 구현했던 것 참고
   
       def size(self):
           return self.data.nodeCount
   
   
       def isEmpty(self):
           return self.data.nodeCount == 0
   
   
       def enqueue(self, item):
           node = Node(item)
           self.data.insertAt(self.data.nodeCount+1, node)
   
   
       def dequeue(self):
           return self.data.popAt(1)
   
   
       def peek(self):
           return self.data.head.next.data
   
   ```

   - 연결리스트로 구현한 큐의 연산 복잡도

     | 연산      | 복잡도 |
     | --------- | ------ |
     | size()    | O(1)   |
     | isEmpty() | O(1)   |
     | enqueue() | O(1)   |
     | dequeue() | O(1)   |
     | peek()    | O(1)   |

     - dequeue 의 경우 배열으로 구현했을 때의 시간복잡도와 다르게 head값만 바꿔주면 되기 때문에 복잡도는O(1)이 된다. 
     - [참고한 사이트](https://cs.stackexchange.com/questions/105029/what-is-the-time-complexity-of-enqueue-and-dequeue-of-a-queue-implemented-with-a)



<br/><br/>

