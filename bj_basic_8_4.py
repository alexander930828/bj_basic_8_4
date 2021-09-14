#1

a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    print(int(a/(c-b)+1))

# 2

n = int(input())

c = 1

while n > 1:
    n -= (6 * c)
    c += 1

print(c)