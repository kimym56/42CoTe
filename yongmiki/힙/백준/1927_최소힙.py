import heapq
import sys
N = int(sys.stdin.readline())
heap = []
for _ in range(N):
  x = int(sys.stdin.readline())
  if x > 0 :
    heapq.heappush(heap,x)
  elif x ==0:
    if len(heap) == 0:
      print(0)
    else :
      y = heapq.heappop(heap)
      print(y)
