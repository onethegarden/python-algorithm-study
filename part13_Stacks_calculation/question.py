'''
인자로 주어진 문자열 expr 은 소괄호와 사칙연산 기호, 그리고 정수들로만 이루어진 중위 표현 수식입니다. 
함수 solution() 은 이 수식의 값을 계산하여 그 결과를 리턴하도록 작성되어 있습니다. 
이 함수는 차례로 splitTokens(), infixToPostfix(), 그리고 postfixEval() 함수를 호출하여 이 수식의 값을 계산하는데,

splitTokens() - 강의 내용에서와 같은 코드로 이미 구현되어 있습니다.
infixToPostfix() - 지난 강의의 연습문제에서 작성했던 코드를 수정하여, 문자열이 아닌 리스트를 리턴하도록 작성합니다.
postfixEval() - 이번 강의의 연습문제입니다. 함수의 내용을 완성하세요.
즉, 두 개의 함수 infixToPostfix() 와 postfixEval() 을 구현하는 연습입니다. 스택을 이용하기 위하여 class ArrayStack 이 정의되어 있으므로 그것을 활용하세요.

[참고] Python 에는 eval() 이라는 built-in 함수가 있어서, 이 함수에 문자열을 인자로 전달하면, 그 문자열을 그대로 Python 표현식으로 간주하고 계산한 결과를 리턴하도록 되어 있습니다. 
이 built-in 함수 eval() 을 이용하면 이 연습문제는 전혀 직접 코드를 작성하지 않고도 정답을 낼 수 있을 것이지만, 스택을 이용하여 중위표현식을 계산하는 프로그래밍 연습을 위한 것이니, 
강의 내용에서 설명한 절차를 수행하도록 코드를 작성해 보세요.

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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    for i in tokenList:
        if i not in prec and i != ')':
            postfixList.append(i)
        else:
            if i=='(':
                opStack.push(i)
            elif i==')':
                while opStack.peek() != '(':
                    postfixList.append(opStack.pop())
                opStack.pop()
            else:
                if not opStack.isEmpty():
                    while prec[opStack.peek()] >= prec[i]:
                        postfixList.append(opStack.pop())
                        if opStack.isEmpty():
                            break
                    opStack.push(i)
                else:
                    opStack.push(i)

    while not opStack.isEmpty():
      postfixList.append(opStack.pop())

    print(f"후위표현식 변환 결과 :  {postfixList}")
    return postfixList


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


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val

test = {
  "5 + 3" : 8,
  "(1 + 2) * (3 + 4)" : 21,
  "7 * (9 - (3+2))" : 28
}

for key, value in test.items():
  print(f"expr : {key}, result : {value}, answer : {solution(key)}\n")
