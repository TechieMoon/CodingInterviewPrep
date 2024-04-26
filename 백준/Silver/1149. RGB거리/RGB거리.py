def min_cost(costs):
    n = len(costs)
    
    result = [[0] * 3 for _ in range(n)]

    result[0][0] = costs[0][0]
    result[0][1] = costs[0][1]
    result[0][2] = costs[0][2]

    for i in range(1, n):
        result[i][0] = min(result[i-1][1], result[i-1][2]) + costs[i][0]
        result[i][1] = min(result[i-1][0], result[i-1][2]) + costs[i][1]
        result[i][2] = min(result[i-1][0], result[i-1][1]) + costs[i][2]

    return min(result[-1])

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

print(min_cost(costs))