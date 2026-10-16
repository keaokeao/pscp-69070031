"""ใคร"""
m = int(input())
n = int(input())
setm = set()
intersect_result = set()
for _ in range(m):
    code = int(input())
    setm.add(code)
for _ in range(n):
    code = int(input())
    if code in setm:
        intersect_result.add(code)
if not intersect_result:
    print("Nope")
else:
    for i in sorted(intersect_result, reverse=True):
        print(i)
