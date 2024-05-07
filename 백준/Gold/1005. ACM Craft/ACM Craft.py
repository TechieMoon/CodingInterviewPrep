import sys
from collections import deque
input = sys.stdin.readline

def acm_craft():
    results = []
    T = int(input().strip()) 
    for _ in range(T):
        N, K = map(int, input().strip().split())
        build_times = list(map(int, input().strip().split()))
        graph = [[] for _ in range(N)]
        degree = [0] * N
        for _ in range(K):
            start, end = map(int, input().strip().split())
            start -= 1
            end -= 1
            graph[start].append(end)
            degree[end] += 1
        
        # 최종 건물 번호
        target = int(input().strip()) - 1
        
        dp = [0] * N
        q = deque()

        # 진입 차수가 0인 노드 큐에 추가 (시작 건물 찾기)
        for i in range(N):
            if degree[i] == 0:
                q.append(i)
                dp[i] = build_times[i]
        
        # 위상 정렬 실행
        while q:
            current = q.popleft()
            if current == target:
                results.append(dp[target])
                break
            for next_node in graph[current]:
                if dp[next_node] < dp[current] + build_times[next_node]:
                    dp[next_node] = dp[current] + build_times[next_node]
                degree[next_node] -= 1
                if degree[next_node] == 0:
                    q.append(next_node)
    
    return results

# 결과 출력
answer = acm_craft()
for line in answer:
    print(line)
