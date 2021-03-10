'''
이미 주어진 코드 (class Node 와 class BinaryTree 에 의하여) 의 구조를 따르는 이진 트리 (binary tree) 에 대하여, 트리의 깊이 (depth) 를 구하는 연산의 구현을 완성하세요.

초기 코드에 pass 로만 되어 있는 class Node 의 depth() 메서드와 class BinaryTree 의 depth() 메서드를 구현합니다. 코드의 다른 부분은 수정할 필요가 없습니다.

참고로 할 수 있도록, 강의에서 소개한 size() 메서드들 (class Node 와 class BinaryTree 에 대해서) 을 그대로 두었습니다. 문제로 주어진 depth() 연산도 매우 비슷한 식으로 구현할 수 있으니 참고로 삼으세요.

[참고] 실행 을 눌렀을 때 통과하는 것은 아무 의미 없습니다.
또한, solution() 함수는 테스트에 영향을 미치므로 수정하지 말고 그대로 두세요.

'''


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1


    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0

        return max(l, r) +1


class BinaryTree:

    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0


    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0
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
print(btree.size())
print(btree.depth())
