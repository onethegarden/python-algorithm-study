# 재귀 알고리즘 (recursive algorithms) 



<br/><br/>



### 1. 재귀 알고리즘의 응용

##### 1. 조합의 수 : n 개의 서로 다른 원소에서 m개를 택하는 경우의 수

##### 2. 하노이의 탑 : 크기 순서로 쌓여 있는 원반을 한 막대기에서 다른 막대기로 옮기기

##### 3. 피보나치 순열



<br/>

### 2. 이진탐색 알고리즘의 재귀적 구현

``````python
def solution(L, x, l, u):
  print(l, u)
  if l > u: 
    return -1
  mid = (l + u) // 2
  if x == L[mid]:
    return mid
  elif x < L[mid]:
    return solution(L, x, l, mid-1 )
  else:
    return solution(L, x, mid+1, u)
``````

- **```if l > u``` 인 이유** 

-  ```solution([1,2,3,4], 4, 0, 3)``` 로 실행했을 때 2째 줄 print에 찍힌 것을 보면

  ```
  0 3
  2 3
  3 3 
  4의 위치는 : 3
  ```

  이므로 마지막에 ```l```과 ```u```가 같아지는 순간도 비교를 해야 하므로 ```l > u```가 맞음

