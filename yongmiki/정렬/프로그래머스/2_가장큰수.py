def solution(num): 
    num = list(map(str, num)) 
    num.sort(key = lambda x : x*3, reverse = True) 
    return str(int(''.join(num)))

#출처: https://wooaoe.tistory.com/82 [개발개발 울었다]



""" 시간초과
import itertools

def solution(numbers):
    return max(list(map(''.join,itertools.permutations(map(str,numbers)))))
"""
