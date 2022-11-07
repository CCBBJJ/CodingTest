n,m = map(int, input().split())

s = []

def dfs(tmp):
    if len(s) == m:
        return print(' '.join(map(str, s)))
    for i in range(1,n+1): # 맨 앞자리
        if tmp <= i:
            s.append(i)
            dfs(i)
            s.pop()
        
dfs(0)