'''
이진 트리를 구현한 클래스인 class BinaryTree 에 대하여 넓이 우선 순회 (breadth first traversal) 를 구현하는 메서드 bft() 를 완성하세요.

class ArrayQueue 는 배열 (python list) 을 이용하여 구현한 큐 (queue) 의 추상적 자료구조입니다. 이것을 이용하여 넓이 우선 순회 알고리즘을 구현하세요.

[참고 1] solution() 함수의 구현은 그대로 두세요. 이것을 없애면 테스트가 되지 않습니다.

[참고 2] "코드 실행" 을 눌렀을 때 통과하는 것은 아무런 의미가 없습니다.

1. (초기화) traversal <- 빈 리스트, q <- 빈 큐
2. 빈 트리가 아니면, root node를 q에 추가(enqueue)
3. q가 비어있지 않은 동안
   1. node <- q 에서 원소를 추출
   2. node를 방문
   3. node의 왼쪽, 오른쪽 자식이 있으면 q에 추가
4. q가 빈 큐가 되면 모든 노드 방문 완료
'''

class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r


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