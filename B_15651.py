n,m = map(int, input().split())

s = []

def dfs():
    if len(s) == m:
        return print(' '.join(map(str, s)))
    for i in range(1,n+1): # 맨 앞자리
        s.append(i)
        dfs()
        s.pop()   
dfs()