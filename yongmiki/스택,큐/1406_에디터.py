import sys
input = sys.stdin.readline

str1 = list(input().strip())
str2 = []
N = int(input())
for _ in range(N):
  temp = input()
  op=temp[0]
  if op == 'L' and len(str1):
    str2.append(str1.pop())
  elif op == 'D' and len(str2):
    str1.append(str2.pop())
  elif op == 'B' and len(str1):
    str1.pop()
  elif op == 'P':
    str1.append(temp[2])
str2.reverse()
print(''.join(str1+str2))
