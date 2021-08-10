import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville)>1 :
        min_scov = heapq.heappop(scoville)
        if min_scov > K:
            return answer
        heapq.heappush(scoville,min_scov+heapq.heappop(scoville)*2)
        answer += 1
    if heapq.heappop(scoville) > K:
        return answer
    return -1
