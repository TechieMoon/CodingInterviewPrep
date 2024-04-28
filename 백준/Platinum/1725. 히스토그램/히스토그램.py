def largest_rectangle_area(heights):
    heights.append(0)
    stack = []
    max_area = 0

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    heights.pop() 
    return max_area

N = int(input())
heights = [int(input()) for i in range(N)]

print(largest_rectangle_area(heights))