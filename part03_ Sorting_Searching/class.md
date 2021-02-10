# 정렬(Sort), 탐색(Search)

> 정렬 : 복수로 주어진 데이터를 정해진 기준에 따라 새로 늘어놓는 작업
>
> 탐색 : 복수로 주어진 데이터에서 특정 원소를 찾아내는 작업

<br/><br/>



### 1. 정렬의 대표적인 종류

##### 1. ```sorted()``` : 파이썬의 내장 함수

##### 2. ```.sort()``` : list에 쓸 수 있는 메서드

<br/>

### 2. 탐색의 대표적인 종류

##### 1. 선형탐색(linear search) :  순차적으로 모든 요소를 탐색. 배열의 길이에 비례함

##### 2. 이진탐색(binary search) : 탐색하려는 배열이 이미 정렬되어 있는 경우에만 적용.



### 이진탐색 구현

- L : 정렬된 배열,  x : 찾는 값

```python
def solution(L, x):
    lower = 0
    upper = len(L)-1
    idx = -1

    while lower <= upper: 
        middle = (lower + upper)//2
        if L[middle] == x :
            idx = middle
            break
        elif L[middle] < x: 
            lower = middle + 1
        else:
            upper = middle - 1
    return idx

#테스트 코드
print(solution([2, 3, 5, 6, 9, 11, 15], 6))
print(solution([2, 5, 7, 9, 11], 4))
print(solution([1, 2, 3], 3))
```

- lower와 upper를 재설정할 때 ```middle + 1``` 과 ```middle - 1``` 을 각각 설정해주는게 처음에는 이해가 안됐었는데 테스트 코드 세 번 째 줄의 

  ``` python
  print(solution([1, 2, 3], 3))
  ```

  이 코드를 생각해보면 

  ```python
  1. middle = lower+upper #middle은 1
  2. L[middle] 2 은 x보다 작음
  3. elif문의 lower = middle+1 #lower = 1+1 =2
  #(만약 여기서 +1을 안해주면 lower 값은 1이 되어 while문을 탈출 할 수 없음)
  ```

  

