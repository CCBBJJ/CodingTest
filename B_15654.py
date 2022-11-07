n,m = map(int, input().split())

s = list(sorted(list(map(int, input().split()))))
em_list = []

def dfs():
    if len(em_list) == m:
        return print(' '.join(map(str, em_list)))
    for i in range(len(s)): # 맨 앞자리
        if s[i] not in em_list:
            em_list.append(s[i])
            dfs()
            em_list.pop()
        
dfs()