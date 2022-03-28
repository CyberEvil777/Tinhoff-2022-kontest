value = int(input())
count = 0
while value % 10 == 0:
    count += 1
    value //= 10
print(count)