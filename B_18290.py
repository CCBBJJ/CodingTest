N, M, K = map(int, input().split())

map = [list(map(int, input().split()))for i in range(N)]

check = [[False]*M for i in range(N)]

print(map)
print(check)