num_len = int(input())
num_str = input()

sum = 0
for i in range(num_len):
    sum += int(num_str[i])
    
print(sum)