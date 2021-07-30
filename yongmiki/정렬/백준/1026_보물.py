import sys

N = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_sortlst = sorted(a_list)
b_sortlst = sorted(b_list, reverse=True)
sum = 0
for i in range(0,N):
  sum += a_sortlst[i]*b_sortlst[i]
print(sum)
