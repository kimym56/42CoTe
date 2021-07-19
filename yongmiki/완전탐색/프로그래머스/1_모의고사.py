def solution(answers):
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    c1,c2,c3,count = 0,0,0,0
    for ans in answers:
        if num1[count%len(num1)] == ans:
            c1 = c1 + 1
        if num2[count%len(num2)] == ans:
            c2 = c2 + 1
        if num3[count%len(num3)] == ans:
            c3 = c3 + 1
        count = count + 1
    answer = []
    if max(c1,c2,c3) == c1:
        answer.append(1)
    if max(c1,c2,c3) == c2:
        answer.append(2)
    if max(c1,c2,c3) == c3:
        answer.append(3)
    return answer
