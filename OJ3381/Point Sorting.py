"""sort"""
t = int(input())

for _ in range(t):
    n = int(input())
    points = []
    for _ in range(n):
        line = input().split()
        x = int(line[0])
        y = int(line[1])
        points.append((x, y))
    points.sort(key=lambda p: (p[0] + p[1], -p[1]))
    for x, y in points:
        print(x, y)
