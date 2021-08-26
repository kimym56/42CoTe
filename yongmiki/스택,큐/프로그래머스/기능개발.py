import math
def solution(progresses, speeds):
    que = []
    answer = []
    for i in range(len(progresses)):
        que.append(math.ceil((100-progresses[i])/speeds[i]))
    maxN = que[0]
    count = 1
    for i in range(1,len(que)):
        if que[i]>maxN:
            answer.append(count)
            maxN=que[i]
            count=1
        else:
            count += 1
    answer.append(count)
    return answer
