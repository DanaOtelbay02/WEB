n = int(input())
i = 0

while i <= n:
    j = 0
    m = 1
    while j < i:
        m *= 2
        j += 1
    if(m >= n):
        print(i)
        break
    i += 1