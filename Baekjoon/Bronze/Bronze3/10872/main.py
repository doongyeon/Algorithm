n = int(input())

if n == 0:
    print(1)
else:
    result = 1
    for i in range(n):
        result *= (i + 1)
    print(result)