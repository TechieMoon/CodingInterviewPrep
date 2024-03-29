from collections import deque

def recursive(N, K):
    length = 100001
    
    visited = [0] * length
    
    q = deque([N])
    
    while q:
        current = q.popleft()
        
        if current == K:
            return visited[current]
        
        for next in (current - 1, current + 1, current * 2):
            if 0 <= next < length and not visited[next]:
                visited[next] = visited[current] + 1
                q.append(next)

N, K = map(int, input().split())

print(recursive(N, K))
