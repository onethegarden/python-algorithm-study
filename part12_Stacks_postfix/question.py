'''
중위 표기법을 따르는 수식 S 가 인자로 주어질 때, 이 수식을 후위 표기법을 따르는 수식으로 변환하여 반환하는 함수 solution() 을 완성하세요.

인자로 주어지는 수식 문자열 S 는 영문 대문자 알파벳 한 글자로 이루어지는 변수 A - Z 까지와 4칙연산을 나타내는 연산자 기호 +, -, *, /, 그리고 여는 괄호와 닫는 괄호 (, ) 로 이루어져 있으며 공백 문자는 포함하지 않는 것으로 가정합니다. 또한, 올바르게 구성되지 않은 수식은 인자로 주어지지 않는다고 가정합니다. (수식의 유효성은 검증할 필요가 없습니다.)

문제에서 미리 주어진, 연산자의 우선순위를 표현한 python dict 인 prec 을 활용할 수 있습니다.

또한, 스택의 기초 강의에서 이미 구현한, 배열을 이용한 스택의 추상적 자료 구조 코드가 이미 포함되어 있으므로 그대로 이용할 수 있습니다.
'''


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
