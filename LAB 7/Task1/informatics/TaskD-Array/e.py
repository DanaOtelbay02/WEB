n = int(input())
arr = list(map(int, input().split()))

check = False

for i in range(1, n):
    if(arr[i] > 0 and arr[i-1] > 0) or (arr[i] < 0 and arr[i-1] < 0):
        check = True

if check:
    print("YES")
else:
    print("NO")