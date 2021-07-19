import math
def fun_2(a,b,c):
    return ((-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a))

def solution(brown, yellow):
    # 2i+2j+4 = b
    # ij = y
    # 2i^2 + (4-b)i+ 2y = 0
    x = fun_2(2,4-int(brown),2*int(yellow))
    i = min(x)
    j = max(x)
    print(x,i,j)
    answer = [j+2,i+2]
    return answer
