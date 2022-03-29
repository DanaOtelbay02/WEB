# def double_power(a, n):
#     if n == 0:
#         return 1
#     else:
#         return a * double_power(a, n-1)

def power(a, n):
    if n == 0:
        return 1
    res = power(a * a, n // 2)
    if n % 2:
        res *= a
    return res

inp = list(map(float, input().split()))

# print(double_power(inp[0], int(inp[1])))
print(power(inp[0], int(inp[1])))
