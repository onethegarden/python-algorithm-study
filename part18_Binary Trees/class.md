# 이진 트리(Binary Trees)



>트리에 포함되는 모든 노드의 차수가 2 이하인 트리

<br/><br/>

### 1. 이진트리의 추상적 자료구조

- 연산의 정의
  - size() : 현재 트리에 포함되어 있는 노드 수
  - depth() : 현재 트리의 깊이 (또는 높이; height)를 구함
  - 순회(traversal)



<br/><br/>

### 2. 이진트리의 구현

1. Node 정의
   - Data
   - Left Child
   - Right Child

```python
class Node:
	def __init__(self, item):
	self.data = item
	self.left = None
	self.right = None
      
    def size(self): # 재귀적인 방법으로 구할 수 있음
        # 전체 이진트리의 size = left subtree의 size() + right subtree의 size() + 자기자신
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0 
        return l + r + 1
    
    def depth(self):  # 전체 depth = leftSubtree depth 와 right Subtree depth 중 더 큰 것
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return max(l, r) + 1
```



2. 이진트리의 구현

```python
class BinaryTree:
	def __init__(self,r):
		self.root = r
        
    def size(self): # 재귀적인 방법으로 구할 수 있음
        if self.root:
            return self.root.size()
        else:
            return 0
        
    def depth(self) : # 전체 depth = leftSubtree depth 와 right Subtree depth 중 더 큰 것
        if self.root:
            return self.root.depth()
        else:
            return 0
```





### 💫 이진트리의 순회 (Traversal) 



#### 깊이 우선 순회(depth first traversal)

- **중위 순회 (in-order traversal)**

  ![중위순회](https://user-images.githubusercontent.com/51187540/110563093-186bf700-818e-11eb-9e03-632feabce7c7.PNG)

  - 순회의 순서 : 
    1. left subtree
    2. 자기자신
    3. right subtree
  - 주의할 점 : 6번의 경우 7번이 오른쪽에 있으므로 6번을 먼저 순회
  - 구현 방법 : node에 자기자신을 root로 하는 서브트리에 대해 재귀적인 방법으로

  ```javascript
  class Node:
  	def inorder(self):
  		traversal = [] #순회 하는걸 넣기
  		if self.left: #왼쪽이 있을 때 
  			traversal += self.left.inorder() # 반환된 리스트에 이어붙임
  			traversal.append(self.data) # 자기자신을 붙이기
  			if self.right:
  				traversal += self.right.inorder() # 오른쪽 서브트리가 있으면 붙이기
  				
  			return traversal
  ```

  ```python
  class BinaryTree:
      def inorder(self):
          if self.root:
              return self.root.inorder()
          else:
              return []
  ```

  

  

- ** 전위 순회 (pre-order traversal) **

  ![전위순회](https://user-images.githubusercontent.com/51187540/110564159-bd3b0400-818f-11eb-9ec4-5b293aa52dc3.PNG)

  - 순회의 순서 : 
    1. 자기자신
    2. left subtree
    3. right subtree
  - 순회의 순서를 고려하여 순환할 배열에 넣어주면 된다.

  ```python
  class Node:
      def preorder(self):
          traversal = []
          traversal.append(self.data)
          if self.left:
              traversal += self.left.preorder()
          if self.right:
              traversal += self.right.preorder()
          return traversal
  ```

  ```python
      def preorder(self):
          if self.root:
              return self.root.preorder()
          else:
              return []
  ```

  



- **후위 순회 (post-order traversal)**

  ![후위순회](https://user-images.githubusercontent.com/51187540/110564419-1f940480-8190-11eb-82be-80f805169bc0.PNG)

  - 순회의 순서 : 
    1. Left subtree
    2. Right subtree
    3. 자기 자신

  - 

  ```python
  class Node:
      def postorder(self):
          traversal = []
          if self.left:
              traversal += self.left.postorder()
          if self.right:
              traversal += self.right.postorder()
          traversal.append(self.data)
  
          return traversal
  ```

  ```python
      def postorder(self):
          if self.root:
              return self.root.postorder()
          else:
              return []
  ```





- 넓이 우선 순회 (breadth first traversal)

  - -> 다음 강의 

  

