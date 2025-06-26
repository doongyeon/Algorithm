n, x = map(int, input().split())
fir_list = list(map(int, input().split()))

filter_list = list(filter(lambda a : a < x, fir_list))
print(*filter_list)