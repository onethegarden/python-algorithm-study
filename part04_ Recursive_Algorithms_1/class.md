# Recursive algorithms (재귀 알고리즘)

> 같은 알고리즘을 반복적으로 적용함으로써 풀어내는 것
>
> -> 하나의 함수에서 자기 자신을 다시 호출하여 작업을 수행

<br/>

### 예1) 1부터 n까지 모든 자연수의 합 구하기

- 자기 자신을 다시 호출해서 작성

```python
def sum(n):
	return n + sum(n - 1)
```

-> 이렇게 작성할 경우 -1, -2, -3번까지 무한대로 더해지기 때문에 **재귀 호출의 종결**조건을 걸어 놓아야 한다.

```python
def sum(n):
    if n <= 1:
        return n
    else:
		return n + sum(n - 1)
```

<br/><br/>

### 예2) Factorial (n!)

```python
def factorial(n):
	if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
```





### 예3) Fibonacci

> F0 = 0
>
> F1 = 1
>
> Fn = Fn - 1 + Fn - 2, n >= 2
>
> ```ex) 0, 1, 1, 2, 3, 5, 8, 13, 21,,,,```

1. 재귀적으로 

```python
def solution(x):
    if x <= 1 : #1과 같거나 작을 때를 유의해야함 x < 2
        return x
    else:
        return solution(x-1)+solution(x-2)
```

2. while문

```python
def solution(x):
    a = 0
    b = 1
    sum = a+b
    
    if x < 2 :
        return x
    else :
        while x > 2 : # 1과 0은 미리 선언
            a = b
            b = sum
            sum = a+b  
            x = x-1
    return sum
```

