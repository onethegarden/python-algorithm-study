# 후위 표기 수식 계산



### 1. 중위 표기법과 후위 표기법

중위표기법```(A+B)*(C+D)``` ->  후위표기법```AB+CD+*```

<br/><br/>



### 2. 후위 표기식의 계산

```AB-CD+*```

- 연산자가 나오기 전까지 push
- 연산자가 나오면 pop하여 연산 실행 (- or %는 순서를 주의한다 )



#### 스택 후위 표기식 계산

1. ##### 설계 

   - 왼쪽부터 한 글자씩 읽기 
   - 피연산자이면 push
   - 연산자를 만나면 스택에서 pop (1) ->, 또 pop(2) -> 2연산, 1을 계산, 이 결과를 스택에 push
   - 수식의 끝에 도달하면 스택에서 pop -> 이게 결과

<br/>

2. ##### 풀이 : 매개변수 tokenList 는 list다

   ```python
   def postfixEval(tokenList):
       valStack = ArrayStack()
       for t in tokenList:
           if type(t) is int:
               valStack.push(t)
           elif t == '*':
               valStack.push(valStack.pop()*valStack.pop())
           elif t == '/':
               last = valStack.pop()
               pre = valStack.pop()
               valStack.push(pre/last)
           elif t == '+':
               valStack.push(valStack.pop()+valStack.pop())
           elif t == '-':
               last = valStack.pop()
               pre = valStack.pop()
               valStack.push(pre-last)
       return valStack.pop()
   
   ```

<br/>

<br/>

3. ##### 💥주의할 점

   - ```-``` 와 ```/```일 때 ```pop()``` 순서를 유의해야 한다. 

   - ```/```  나누기 예시

     ```python
     elif t == '/':
     	last = valStack.pop()
         pre = valStack.pop()
         valStack.push(pre/last)
     ```

     
