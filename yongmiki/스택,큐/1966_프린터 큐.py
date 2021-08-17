import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N,M = input().split()
  temp = input().split()
  maxN = max(temp)
  que = list(enumerate(temp))
  count = 1
  while True:
    if que[0][1] < maxN:
      que.append(que.pop(0))
    elif int(que[0][0]) != int(M):
      count += 1
      que.pop(0)
      maxN = max(que,key=lambda x:x[1])[1]
    else:
      print(count)
      break;


