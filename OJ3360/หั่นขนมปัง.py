"""bread"""
w, h, m, n = map(int, input().split())
x = [0] + list(map(int, input().split())) + [w]
y = [0] + list(map(int, input().split())) + [h]
widths = []
for i in range(len(x) - 1):
    widths.append(x[i+1] - x[i])
heights = []
for i in range(len(y) - 1):
    heights.append(y[i+1] - y[i])
widths.sort(reverse=True)
heights.sort(reverse=True)
max1 = widths[0] * heights[0]
max2 = max(widths[0] * heights[1], widths[1] * heights[0])
print(max1, max2)
