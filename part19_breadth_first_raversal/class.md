## 이진트리의 넓이 우선 순회 (BFS; Breadth First Traversal)

<br/><br/>



### 1. 원칙

- 수준(level)이 낮은 노드를 우선으로 방문
- 같은 수준의 노드들 사이에서는, 부모 노드의 방문순서에 따라 방문
- 같은 부모면 왼쪽 자식 노드를 오른쪽 자식보다 먼저 방문



-> 재귀적 방법은 적당하지 않음





### 2. 설계

![넓이우선순회](https://user-images.githubusercontent.com/51187540/110735478-378d8600-826d-11eb-9840-ad4378e887e6.PNG)



- 한 노드를 방문했을 때,
  - 나중에 방문할 노드들을 순서대로 기록해 두어야 함.
  - -> **Queue를 이용**



![image](https://user-images.githubusercontent.com/51187540/110735702-a7037580-826d-11eb-985f-71aa94cea5cc.png)

​	

- 큐에서 꺼내기 전에 자식노드를 왼쪽부터 넣음





### 4. 구현

1. (초기화) traversal <- 빈 리스트, q <- 빈 큐
2. 빈 트리가 아니면, root node를 q에 추가(enqueue)
3. q가 비어있지 않은 동안
   1. node <- q 에서 원소를 추출
   2. node를 방문
   3. node의 왼쪽, 오른쪽 자식이 있으면 q에 추가
4. q가 빈 큐가 되면 모든 노드 방문 완료

```python
class BinaryTree:
        def bft(self):
        traversal = []
        que = ArrayQueue()
        if self.root:
            que.enqueue(self.root)
            while que.size()>0:
                deque = que.dequeue()
                if deque.left:
                    que.enqueue(deque.left)
                if deque.right:
                    que.enqueue(deque.right)
                traversal.append(deque.data)

        return traversal
```



- 테스트 코드

```python

'''
        1
    2       3
  4   5    6
  7        
'''
node7 = Node(7)

node6 = Node(6)

node5 = Node(5)

node4 = Node(4)
node4.left = node7

node3 = Node(3)
node3.left = node6

node2 = Node(2)
node2.left = node4
node2.right = node5

node1 = Node(1)
node1.left = node2
node1.right = node3

btree = BinaryTree(node1)

print('start')
print(btree.bft()) # 1234567
```

