def find_next_greater_element(array, N):
    # 초기에는 모두 -1로 초기화(큰 수가 없는 경우는 -1)
    result = [-1] * N
    # 처음에는 스택 비우기
    stack = []
    # 역추적하기
    for i in range(N - 1, -1, -1):
        # 스택에서 꺼내고 작으면 버리기
        while stack and stack[-1] <= array[i]:
            stack.pop()
        # 스택에는 현재값보다 큰 것 밖에 없고 그 중 가장 작은 값이 위에 있음
        # 작은 걸 다 버렸으니 스택에서 top value를 저장, 없으면 패스
        if stack:
            result[i] = stack[-1]
        # 현재 값 스택에 넣기
        stack.append(array[i])

    return result

N = int(input())
array = list(map(int, input().split()))

result = find_next_greater_element(array, N)
print(*result)