def can_pass_road(road, N, L):
    i = 0
    used = [False] * N  # Track where slopes are placed

    while i < N - 1:
        if road[i] == road[i + 1]:
            i += 1
            continue
        elif abs(road[i] - road[i + 1]) > 1:
            return False 
        elif road[i] + 1 == road[i + 1]:
            if i - L + 1 < 0:
                return False
            for j in range(i - L + 1, i + 1):
                if road[j] != road[i] or used[j]:
                    return False
            for j in range(i - L + 1, i + 1):
                used[j] = True
            i += 1
        elif road[i] - 1 == road[i + 1]:
            if i + L > N - 1:
                return False 
            for j in range(i + 1, i + L + 1):
                if road[j] != road[i + 1] or used[j]:
                    return False
            for j in range(i + 1, i + L + 1):
                used[j] = True
            i += L
        else:
            return False

    return True

def num_roads(map, N, L):
    count = 0

    for i in range(N):
        if can_pass_road([map[i][j] for j in range(N)], N, L):
            count += 1
        if can_pass_road([map[j][i] for j in range(N)], N, L):
            count += 1

    return count

N, L = map(int, input().split())
map1 = [list(map(int, input().split())) for _ in range(N)]

answer = num_roads(map1, N, L)
print(answer)
