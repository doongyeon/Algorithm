test_num = input()
n = []
m = []
for _ in range(int(test_num)):
    a = input()
    a = a.split()
    n.append(int(a[0]))
    m.append(int(a[1]))

ans = [[0 for j in range(30)] for i in range(30)]

for i in range(30):
    ans[0][i] = 0
    ans[1][i] = i

for i in range(30):
    for j in range(30):
        if i == 0:
            ans[i][j] = 0
            continue
        if i > j:
            ans[i][j] = 0
            continue
        if i == 1:
            ans[i][j] = j
            continue
        if i == j:
            ans[i][j] = 1
            continue
        else:
            ans[i][j] = sum(ans[i-1][0:j])

for i in range(int(test_num)):
    print(ans[n[i]][m[i]])

