"""dog mai"""
l, n = map(int, input().split())
low, high = 1, 2 * 10**9
ans = high
while low <= high:
    mid = (low + high) // 2
    d = mid * l
    total_slots = (d * (d + 1)) // 2
    if total_slots >= n:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1
print(ans)
