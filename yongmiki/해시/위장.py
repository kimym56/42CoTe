def solution(clothes):
    answer = 1
    from collections import Counter
    cnt = Counter([kind for name,kind in clothes])
    for i in cnt.values():
        answer *= (i+1)
    return answer-1
