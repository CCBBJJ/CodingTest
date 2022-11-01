T = int(input())
q_list = []

for _ in range(T):
    q_list.append(list(map(int, input().split())))

for i in range(T):
    M = q_list[i][0]
    N = q_list[i][1]
    x = q_list[i][2]
    y = q_list[i][3]
    tmp_x = 1
    tmp_y = 1
    count = 1
    while tmp_x == M and tmp_y == N:
        tmp_x += 1
        tmp_y += 1
        count += 1
        if tmp_x > M:
            tmp_x = 1
        if tmp_y > N:
            tmp_y = 1
        print(f"tmp_x: {tmp_x}, tmp_y: {tmp_y}")
        #if tmp_x == x and tmp_y == y:
        #    break
      
    print(count)