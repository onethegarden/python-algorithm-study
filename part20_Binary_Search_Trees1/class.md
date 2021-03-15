## 이진 탐색 트리(Binary Search Trees)

>모든 노드에 대해서 
>
>왼쪽 서브트리에 있는 데이터는 모두 현재 노드의 값보다 작고
>
>오른쪽 서브트리에 있는 데이터는 모두 현재 노드의 값보다 큰 
>
>성질을 만족하는 이진트리 (중복되는 데이터는 없는 것으로 가정)





### 이진탐색트리

![image](https://user-images.githubusercontent.com/51187540/111118267-e0a8e900-85ab-11eb-939f-2791850b9650.png)

- 정렬된 배열보다 원소와 삽입이 쉬움
- 공간 소요가 큼( 항상 ```O(logn)```의 탐색 복잡도?)
- 트리의 기준이 되는 key를 이용해 데이터를 검색함



### 연산의 정의

- ```insert(key, data)``` : 트리에 주어진 데이터 원소를 추가

- ```remove(key)``` : 특정 원소를 트리로부터 삭제
- ```lookup(key)``` : 특정 원소를 검색
- ```inorder()``` : 키의 순서대로 데이터 원소를 나열
- ```min()```, ```max()``` : 최소 키, 최대 키를 가지는 원소를 각각 탐색



```python
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        
    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal
        
    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self
        
    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else:
            return self, parent
        
    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        else:
            raise KeyError('...')
```

```python
class BinSearchTree:
    def __init__(self):
        self.root = None
        
    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return
        
    def min(self):
        if self.root:
            return self.root.min()
        else:
            return None
        
    def lookup(self):
        if self.root:
            return self.root.lookup(key)
        else:
            return None,None
        
    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)
        
```



### ```lookup()```

- 입력 인자 : 찾으려는 대상 키
- 리턴 : 찾은 노드와, 그것의 부모 노드(각각, 없으면 None으로)

### ```insert()```

- 입력인자 : 키, 데이터원소
- 리턴 : 없음

