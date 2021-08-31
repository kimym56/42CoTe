import heapq
def solution(genres, plays):
    sumA = {}
    que = {}
    answer = []
    for i in range(len(genres)):
        if genres[i] in sumA:
            sumA[genres[i]] += plays[i]
        else:
            sumA[genres[i]] = plays[i]
            que[genres[i]] = []
        heapq.heappush(que[genres[i]],(plays[i],i))

    myset = set(genres)
    print(sumA)
    print(que)
    for g in myset:
        que[g] = sorted(que[g],key=lambda x: (x[0],-x[1]))
    print(que)
    res = sorted(sumA.items(),key=(lambda x:x[1]),reverse=True)
    print(res)
    for i,v in res:
        answer.append(que[i].pop()[1])
        if que[i]:
            answer.append(que[i].pop()[1])

    return answer
