# LinkedList

>추상적 자료구조 (Abstract Data Structures)
>
>각 원소들을 줄줄이 엮어서 관리하는 방법



### Linked List

- Node 로 연결되어 있음

  - 각 노드엔 자신의 값(data) 과 그 다음 값 (next) 의 정보가 저장되어 있다.

  ```python
  class Node:
    def __init__(self, item):
      self.data = item
      self.next = None
  ```

- Linked List 에는 노드의 개수를 알 수 있는 NodeCount와 첫 값 (head), 끝 값(tail) 이 저장되어 있다.

  ```python
  class LinkedList:
    def __init__(self):
      self.nodeCount = 0
      self.head = None
      self.tail = None
  ```

  

### 장점

- 원소의 삭제, 삽입이 선형배열보다 쉽다 (= 빠른 시간 내에 처리가 가능하다)



### 단점

- 데이터 구조 표현에 소요되는 저장공간(메모리) 소요가 크다. 

|                | 배열        | 연결 리스트     |
| -------------- | ----------- | --------------- |
| 저장 공간      | 연속한 위치 | 임의의 위치     |
| 특정 원소 지칭 | 매우 간편   | 선형탐색과 유사 |
| 복잡도         | O(1)        | O(n             |

<br/><br/>

### 1. 연산 정의

	1. 특정 원소 참조 (k 번째)
 	2. 리스트 순회
 	3. 길이 얻기
 	4. 원소 삽입
 	5. 원소 삭제
 	6. 두 리스트 합치기

<br/><br/>

### 2. Linked List  구현

```python
class Node:
  def __init__(self, item):
    self.data = item
    self.next = None

class LinkedList:
  def __init__(self):
    self.nodeCount = 0
    self.head = None
    self.tail = None

  def getAt(self, pos):
    if pos < 1 or pos > self.nodeCount:
      return None
    i = 1
    curr = self.head
    while i < pos:
      curr = curr.next
      i += 1
    return curr

  def traverse(self): # 링크드리스트의 배열을 리턴하는 함수
    if self.nodeCount < 1:
      return []
    
    re_val = []
    current = self.head
    while current != None:
      re_val.append(current.data)
      current = current.next
    return re_val
```



### 3. 테스트

```python

#노드값 지정    
node1 = Node(43)
node2 = Node(85)
node3 = Node(62)
node1.next = node2
node2.next = node3

#링크드리스트 생성
myLink = LinkedList()
myLink.nodeCount = 3
myLink.head = node1
myLink.tail = node3

print(myLink.traverse())
```

