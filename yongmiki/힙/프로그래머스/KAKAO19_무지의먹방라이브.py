import heapq
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    heap = []
    for i in range(len(food_times)):
        heapq.heappush(heap, (food_times[i],i+1))
    prev = 0
    while len(heap) and k > ((heap[0][0]-prev) * len(heap)):
        now = heapq.heappop(heap)[0]
        k -= (len(heap)+1)*(now-prev)
        prev = now
    ans = sorted(heap,key=lambda x:x[1])
    return ans[k%len(ans)][1]
"""
def solution(food_times, k):
    num = 0
    idx = 0
    mft = min(food_times)
    lft = len(food_times)
    if sum(food_times) <= k :
        return -1
    if mft*lft < k:
        k -= mft*lft
        for i in range(lft):
            food_times[i]-= mft
    while num<k+1:
        if food_times[idx%lft] > 0:
            food_times[idx%lft] -= 1
            idx +=1
            num +=1
        else:
            idx += 1
            
    return (idx-1)%lft+1
"""
