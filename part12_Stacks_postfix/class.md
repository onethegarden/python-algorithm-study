# Stack 응용



## 후위표기법 Postfix Notation

>연산자를 두 피연산자 뒤에 쓰는 방법  
>
>괄호를 쓰지 않고도 연산의 우선순위를 수식이 표현할 수 있음
>
>ex) ```A+B``` 를 후위표기법으로 바꾸면 ```AB+```



<br/><br/>

#### 문제 : 스택을 이용해 중위 표기법을 후위 표기법으로 변환하기

1. ##### 설계 

   - 왼쪽부터 한 글자씩 읽기 
   - 피연산자이면 그냥 출력
   - ```(``` 이면 스택에 push
   - ```)``` 이면 ```(``` 이 나올 때까지 pop +출력
   - 연산자이면 스택에서 이보다 높거나 같은 우선순위의 것들을 <u>**모두**</u> pop+출력, 스택이 비거나 우선순위가 i 보다 낮은 연산자가 스택의 꼭대기에 있게 되면 연산자를 스택에 push
   - 스택에 남아있는 연산자는 모두 출력  ```while not opStack.isEmpty()```

<br/>

2. ##### 풀이

   ```python
   #ArrayStack 은 .py 파일 참고
   
   prec = {
       '*': 3, '/': 3,
       '+': 2, '-': 2,
       '(': 1
   }
   
   def solution(S):
       opStack = ArrayStack()
       answer = ''
       for i in S:
         if i not in prec and i != ')':
           answer+= i
         else:
           if i=='(':
             opStack.push(i)
           elif i==')':
             while opStack.peek() != '(':
               answer += opStack.pop()
             opStack.pop()
           else:
             if not opStack.isEmpty():
               while prec[opStack.peek()] >= prec[i]:
                 answer += opStack.pop()
                 if opStack.isEmpty():
                   break
               
               opStack.push(i)
             else:
               opStack.push(i)
   
       while not opStack.isEmpty():
         answer += opStack.pop()
       
       return answer
   ```

<br/>

<br/>

3. ##### 😥시행착오 

   - 연산자일 때의 처음 작성한 코드 

     ```python
     if not opStack.isEmpty():
     	if prec[opStack.peek()] < prec[i]:
     		opStack.push(i)
     	else:
     		answer += opStack.pop()
     		opStack.push(i)
     else:
     	opStack.push(i)
     ```

   - 이 코드는  ```A+B*C-D/E``` 이 케이스에서 ```ABC*DE/-+``` 로 예상 값 ```ABC*+DE/-```  와 다르게 나온다 . 

   - ```+```, ```*``` 순서로 스택에 들어 있는데 -와 비교하면서 제일 위에 있는 값 하나 ```*```만 꺼냈기 때문에 ```+```는 남아있게 된다.

     

   -  🎯 연산자일 때 스택에 들어있는 값이 i보다 우선순위가 높거나 같으면 <u>**모두**</u> 꺼내주어야 했다. 이 때 pop 하다가 stack이 비는 경우를 고려해야 한다.

     ```python
     if not opStack.isEmpty():
     	while prec[opStack.peek()] >= prec[i]:
     		answer += opStack.pop()
     		if opStack.isEmpty(): #꺼내다가 비는 경우를 고려
     			break
                 
     	opStack.push(i)
     
     else:
     	opStack.push(i)
     ```

<br/>

<br/>



4. ##### ⚽ 테스트 코드 

   ```python
   test = {
       '(A+B)*(C+D)': 'AB+CD+*', 
       '(A+(B-C))*D': 'ABC-+D*',
       'A*B+C':'AB*C+',
       'A+B*C':'ABC*+',
       'A+B+C':'AB+C+',
       '(A+B+C)*(D+E)':'AB+C+DE+*',
       'A+B*C-D/E':'ABC*+DE/-' #얘가 아주 중요 
   }
   
   for key, value in test.items():
     answer = solution(key)
     if(answer == value):
       print(f'key: {key}, value: {value}, answer:{answer} 결과 True')
     else:
       print(f'key: {key}, value: {value}, answer:{answer} 결과 False')
   ```

   <br/>

   💻 콘솔 출력 값

   ```
   key: (A+B)*(C+D), value: AB+CD+*, answer:AB+CD+* 결과 True
   key: (A+(B-C))*D, value: ABC-+D*, answer:ABC-+D* 결과 True
   key: A*B+C, value: AB*C+, answer:AB*C+ 결과 True
   key: A+B*C, value: ABC*+, answer:ABC*+ 결과 True
   key: A+B+C, value: AB+C+, answer:AB+C+ 결과 True
   key: (A+B+C)*(D+E), value: AB+C+DE+*, answer:AB+C+DE+* 결과 True
   key: A+B*C-D/E, value: ABC*+DE/-, answer:ABC*+DE/- 결과 True
   ```

   
