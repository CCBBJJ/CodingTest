n,m = map(int, input().split())

s = []

def dfs(a):
    tmp = 0
    if len(s) == m:
        return print(' '.join(map(str, s)))
    for i in range(a,n+1): # 맨 앞자리
        if i not in s:
            s.append(i)
            dfs(i)
            s.pop()   
dfs(1)