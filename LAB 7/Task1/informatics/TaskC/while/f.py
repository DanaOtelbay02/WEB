x = int(input())
y = int(input())

day = 1

while (x < y):
    day += 1
    x += x * 0.1

print(day)