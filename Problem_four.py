t = int(input())
for _ in range(t):
    n, m, s = list(map(int, input().split()))
    print( (m+s-2) % n + 1)
