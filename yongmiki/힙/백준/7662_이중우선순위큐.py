import sys
import heapq
def sync(arr):
  while arr and id[arr[0][1]] == 0:
    heapq.heappop(arr)
    
T = int(sys.stdin.readline())
for _ in range(T):
  max_arr,min_arr = [],[]
  id = [0] * 1000000
  k = int(sys.stdin.readline())
  count = 0
  for i in range(k):
    op, num = map(str, sys.stdin.readline().split())
    if op == 'I':
      heapq.heappush(max_arr, (-1 * int(num), i))
      heapq.heappush(min_arr, (int(num), i))
      id[i] = 1
    else:
      if num == '1':
        sync(max_arr)
        if max_arr:
          id[max_arr[0][1]] = 0
          heapq.heappop(max_arr)
      elif num =='-1':
        sync(min_arr)
        if min_arr:
          id[min_arr[0][1]] = 0
          heapq.heappop(min_arr)
  sync(min_arr)
  sync(max_arr)

  if len(max_arr) == 0:
    print("EMPTY")
  else:
    print(-1 * max_arr[0][0], end =" ")
    print(min_arr[0][0])
