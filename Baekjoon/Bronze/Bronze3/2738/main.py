n, m = map(int, input().split())
mat_a = []
mat_b = []

for _ in range(n):
    cur_row = list(map(int, input().split()))
    mat_a.append(cur_row)
    
for _ in range(n):
    cur_row = list(map(int, input().split()))
    mat_b.append(cur_row)
    
for i in range(n):
    result = [x + y for x, y in zip(mat_a[i], mat_b[i])]
    print(*result)