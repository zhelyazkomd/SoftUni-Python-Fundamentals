nums = input().split(' ')
list = []

for num in nums:
    if int(num) > 0:
        list.append(-int(num))
    else:
        list.append(abs(int(num)))

print(list)
