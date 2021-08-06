import sys
import heapq
N = int(sys.stdin.readline())
left,right = [], []
for _ in range(N):
  num = int(sys.stdin.readline())
  if len(left)==len(right):
    heapq.heappush(left,-num)
  else:
    heapq.heappush(right,num)
  if right and -left[0]>right[0]:
    heapq.heappush(right,-heapq.heappop(left))
    heapq.heappush(left,-heapq.heappop(right))
  print(-left[0])
#https://dirmathfl.tistory.com/273
