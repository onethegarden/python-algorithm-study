'''
입력으로 주어지는 리스트 x 의 첫 원소와 마지막 원소의 합을 리턴하는 함수 solution() 을 완성하세요.
'''

def solution(x):
    return x[0]+x[len(x)-1]

print(solution([1, 2, 3, 4, 5]))