import sys; input = sys.stdin.readline
#입력시간을 단축하자

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
checked = [[False] * M for _ in range(N)]
#[[False]*M]*N은 절대 안된다. [[False]*M]을 똑같이 3개 만드는 것이라서 이후 board[1][2]=True를 선언시, board[모든 행][2]이 True로 바뀐다.

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#상하좌우 일일이 쓰는 것은 불편하니 리스트를 이용하자

max_value = 0
#최대값은 전역 변수로 선언

max_p = max(map(max, board))
#board 중에서 가장 큰 수. 시간 초과 방지를 위한 추가 return 조건에 사용한다

def dfs(i, j, dsum, count):
    global max_value #전역변수 끌어오고
    
    if dsum + max_p * (4 - count) < max_value: #함수 시작마다, 이것을 확인한다. 최댓값 블럭으로 나머지를 채웠는데도 max_value보다 작다면 더 볼 필요가 없는 것이다.
        return
    if count == 4: #탐색 완료 조건
        max_value = max(max_value, dsum)
        return
    for n in range(4): #블럭은 총 4개로 이루어지니까 4번 가야함
        ni = i + move[n][0] 
        nj = j + move[n][1]
        if 0 <= ni < N and 0 <= nj < M and not checked[ni][nj]: # 방문한 블록의 범위와 방문 기록을 확인하자
            if count == 2: # ㅗ 모양의 블록을 처리하기 위한 조건문
                checked[ni][nj] = True #앞 블럭을 방문 처리
                dfs(i, j, dsum + board[ni][nj], count + 1) #앞 블럭을 더한 뒤, 블럭을 옮기지 않고, 다시 탐색한다
                checked[ni][nj] = False # 방문 기록 지우기
            checked[ni][nj] = True #다른 모양 블록을 위해 방문 체크
            dfs(ni, nj, dsum + board[ni][nj], count + 1) #블록을 옮겨 탐색 시작
            checked[ni][nj] = False

for i in range(N):
    for j in range(M):
        checked[i][j] = True #전체적인 블록 이동을 위한 처리
        dfs(i, j, board[i][j], 1)
        checked[i][j] = False

print(max_value)