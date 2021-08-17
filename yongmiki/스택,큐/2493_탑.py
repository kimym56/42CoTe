import sys
input = sys.stdin.readline

n = int(input())
top = list(map(int, input().split()))
stack = []
answer = [0 for i in range(n)]
 
for i in range(n):
    while stack:
        if stack[-1][1] > top[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, top[i]])
 
print(*answer)
"""
import sys
input = sys.stdin.readline

N = int(input())
stk = input().split()
answer = ''
rstk = stk[:] # 6 9 5 7 4
for _ in range(N):
  outg = stk.pop()
  tmp = stk[:]
  check = False
  while len(tmp):
    inc = tmp.pop()
    if outg < inc:
      answer = str(stk.index(inc)+1) +' ' + answer
      check = True
      break;
  if not check :
    answer = '0' + ' '+ answer

  
print(answer)
"""
