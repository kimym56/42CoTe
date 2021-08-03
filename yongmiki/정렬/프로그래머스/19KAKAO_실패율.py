def solution(N, stages):
    stages.sort(reverse=True)
    dic_answer = {}
    answer = []
    for i in range(1,N+1):
        count = stages.count(i)
        length = len(stages)
        for j in range(count):
            stages.pop()
        
        if(length != 0):
            dic_answer[i]=count/length
        else:
            dic_answer[i]=0
    print(dic_answer)
            
    nanswer = sorted(dic_answer.items(),key=(lambda x: x[1]),reverse=True)
    for k in nanswer:
        answer.append(k[0])
    return answer
