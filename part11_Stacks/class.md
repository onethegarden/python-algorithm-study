# Stack 스택

> 마지막 넣었던 것부터 넣은 순서의 역순으로 꺼내지는 자료구조
>
> LIFO : last-in first-out (후입선출 자료구조)



<br/><br/>

#### 1. push : 데이터 원소를 추가하는 작업

#### 2. pop: 데이터 원소를 참조하고 삭제하는 작업



#### 3. 스택 구현 

- 기능 : 
  - size() : 데이터 수
  - isEmpty() 비어있는지  ```size() == 0?```
  - push(x) : 데이터 원소 ```x```  스택에 추가
  - pop() : 가장 나중의 원소 제거, 반환
  - peek()  : 가장 나중에 저장된 데이터 원소를 참조, 제거하지 않음

1. 선형배열 이용

   ```python
   class ArrayStack:
   
   	def __init__(self):
   		self.data = []
   
   	def size(self):
   		return len(self.data)
   
   	def isEmpty(self):
   		return self.size() == 0
   
   	def push(self, item):
   		self.data.append(item)
   
   	def pop(self):
   		return self.data.pop()
   
   	def peek(self):
   		return self.data[-1]
   ```

   

2. 연결 리스트 이용

   ```python
   class LinkedListStack:
   
   	def __init__(self):
   		self.data = DoublyLinkedList()
   
   	def size(self):
   		return self.data.getLength()
   
   	def isEmpty(self):
   		return self.size() == 0
   
   	def push(self, item):
   		node = Node(item)
   		self.data.insertAt(self.size() + 1, node)
   
   	def pop(self):
   		return self.data.popAt(self.size())
   
   	def peek(self):
   		return self.data.getAt(self.size()).data
   ```

   - DoubleLinkedList , Node는 기존에 만들었던 것 참고



<br/><br/>



### 3. 연습문제 - 수식의 괄호 유효성 검사

#### 설계 

- 여는 괄호 '({[' 만나면 스택에 push
- 닫는괄호 ')}]' 만나면 pop
  - 스택이 비어있으면 return false
  - 스택에서 pop , 쌍을 이루는 괄호인지 검사 
- 맨 마지막에 스택이 비어있어야 쌍이 맞는 것



```python
def solution(expr):
    match = {')': '(', '}': '{', ']': '['} #쌍을 이루는 괄호인지
    S = ArrayStack()
    
    for c in expr:
        if c in '({[': #여는 괄호 만나면 push
            S.push(c)
        elif c in match: #닫는 괄호 만나면
            if S.isEmpty(): # 빈 값이면 return False
                return False
            else: #빈 값 아니면 쌍 이루는지 검사
                t = S.pop()
                if t != match[c]:
                    return False
    return S.isEmpty() # stack이 비어있어야 쌍이 맞는 것


##테스트 코드
print(solution('(A+B)-1*{25/1}')) #true
print(solution('(A+B)-1*{25/1'))  #false
```









