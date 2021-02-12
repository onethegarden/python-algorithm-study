'''
인자로 0 또는 양의 정수인 x 가 주어질 때, Fibonacci 순열의 해당 값을 구하여 반환하는 함수 solution() 을 완성하세요.

Fibonacci 순열은 아래와 같이 정의됩니다.
F0 = 0
F1 = 1
Fn = Fn - 1 + Fn - 2, n >= 2

재귀함수 작성 연습을 의도한 것이므로, 재귀적 방법으로도 프로그래밍해 보고, 반복적 방법으로도 프로그래밍해 보시기 바랍니다.
'''

def fibo(x):
  a = 0
  b = 1
  sum = a+b
  if x < 2 :
    return x
  else :
    while x > 2 : # 2번 까지는 미리 선언
      a = b
      b = sum
      sum = a+b  
      x = x-1

  return sum




def fibo2(x):
  if x < 2 : #1과 같거나 작을 때를 유의해야함
    return x
  else:
    return fibo(x-1)+fibo(x-2)


print(fibo(10))
print(fibo2(10))
