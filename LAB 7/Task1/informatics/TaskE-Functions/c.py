def xor(x , y):
    if(x == y):
        return False
    else:
        return True

inp = list(map(int, input().split()))

if(xor(inp[0], inp[1])):
    print(1)
else:
    print(0)