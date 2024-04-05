from collections import deque
            
def bfs(matrix, queue, count):
    while queue:
        count += 1
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for moveRow, moveCol in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= moveRow < M and 0 <= moveCol < N and matrix[moveRow][moveCol] == 0:
                    matrix[moveRow][moveCol] = 1
                    queue.append((moveRow, moveCol))
    for row in matrix:
        if 0 in row:
            return -1
    return count
    
N, M = map(int,input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]

queue = deque()

for i in range(M):
    for j in range(N):
        if matrix[i][j] == 1:
            queue.append((i, j))

print(bfs(matrix, queue, -1))