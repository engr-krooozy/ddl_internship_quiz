import sys
s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
k = [int(keyboards_temp) for keyboards_temp in input().strip().split(' ')]
p = [int(pendrives_temp) for pendrives_temp in input().strip().split(' ')]
ans = -1
for i in k:
    for j in p:
        if i + j <= s and i + j >= ans:
            ans = i + j
print(ans)
