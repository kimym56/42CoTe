import sys
T = int(input())
h_list = []
for i in range(0,T):
  hired = 0
  N = int(input())
  lst = []
  for j in range(0,N):
    a , b = sys.stdin.readline().split()
    lst.append([int(a),int(b)])
    
  sorted_list = sorted(lst, key = lambda x : x[0])
  itv_score = sorted_list[0][1]
  hired += 1
  for k in range(1, N):
    if sorted_list[k][1] < itv_score:
      itv_score = sorted_list[k][1]
      hired += 1
      if itv_score == 1:
        break ;
  h_list.append(hired)
for l in h_list:
  print(l)
