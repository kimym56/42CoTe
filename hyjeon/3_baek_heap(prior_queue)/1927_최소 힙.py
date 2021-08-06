import heapq
import sys
# 이렇게 입력 안 받으면 시간초과
input = sys.stdin.readline

minheap = []
n = int(input())
for i in range(n):
    a = int(input())
    if (a == 0):
        if (len(minheap) == 0):
            print(0)
        else:
            print(heapq.heappop(minheap))
    else:
        heapq.heappush(minheap, a)
