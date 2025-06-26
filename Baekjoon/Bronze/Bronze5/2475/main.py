input_list = list(map(int, input().split()))
input_list = list(map(lambda n: n**2, input_list))
print(sum(input_list) % 10)