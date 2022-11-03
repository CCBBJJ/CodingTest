#점화식을 찾으면 쉽게 해결할 수 있는 문제였다
def cc(A):
  if A == 1:
    return 1
  elif A == 2:
    return 2
  elif A == 3:
    return 4
  else:
    return cc(A-1) + cc(A-2) + cc(A-3)
#그런데 난 못찾았다ㅋ
T = int(input())

list = []

for _ in range(T):
  list.append(int(input()))
for i in range(T):
  print(cc(list[i]))

 