# 우선순위 큐(Priority Queue)



>큐가 FIFO의 방식을 따르지 않고 원소들의 우선순위에 따라 큐에서 빠져나오는 방식
>
>수가 작은 게 우선순위가 높음

<br/><br/>

### 1. 활용

- 운영체제의 CPU 스케줄러



<br/><br/>

### 2. 우선순위 큐의 구현

#### 방법

1. Enqueque 할 때 우선순위 순서를 유지하도록

   -> 1번이 더 유리 

2. Dequeue할 때 우선순위 높은 것을 선택 

   -> 모든 데이터 원소를 살펴봐야 하기 때문에



#### 방식

1. 선형 배열

   -> 2번이 더 시간적으로 유리

2. 연결 리스트 이용 



<br/><br/>

### 3. 양방향 연결리스트의 우선순위 큐 구현

#### 1) enqueue의 구현 

​	- queue에 삽입 시 정렬한다. 

```python
class PriorityQueue:
    def enqueue(self, x):
        newNode = Node(x)
        curr = [빈칸] #시작점
        while [빈칸] and [빈칸]: #끝을 만나지 않는 동안 and 우선순위 비교 조건
            curr = curr.next
        self.queue.[빈칸](curr,newNode) #insertAfter, before로 우선순위에 따른 위치에 삽입
```

- 주의 양방향 연결리스트의 ```getAt()```을 사용하지 않음 -> 원소 하나하나 살피는 연산이 실행되기 때문에 curr 포지션을 이용한다. 
- **구현**

```python
def enqueue(self, x):
        newNode = Node(x)
        curr =  self.queue.head 
        while curr.next.data!= None and x < curr.next.data :
            curr = curr.next
        self.queue.insertAfter(curr, newNode)
```





#### 2) Priority queue 구현

```python
class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr.next.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next.next is not None:
                s += ' -> '
        return s


    def getLength(self):
        return self.nodeCount


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def reverse(self):
        result = []
        curr = self.tail
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        curr = prev.next
        next = curr.next
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return curr.data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        prev = self.getAt(pos - 1)
        return self.popAfter(prev)


    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        self.tail = L.tail

        self.nodeCount += L.nodeCount


class PriorityQueue:

    def __init__(self):
        self.queue = DoublyLinkedList()


    def size(self):
        return self.queue.getLength()

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, x):
        newNode = Node(x)
        curr =  self.queue.head # 제일 먼저 꺼낼 값
        while curr.next.data!= None and x < curr.next.data :
            curr = curr.next
        self.queue.insertAfter(curr, newNode)

    def dequeue(self):
        return self.queue.popAt(self.queue.getLength())

    def peek(self):
        return self.queue.getAt(self.queue.getLength()).data


```





#### 3) 테스트 코드 구현

```python
queue = PriorityQueue()
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(1)

print(queue.size())
print(queue.dequeue())
```

