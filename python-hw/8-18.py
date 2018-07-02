def sum_digit(num):
    number = str(num)

    sum = 0
    for i in range(len(number)):
        sum = sum + int(number[i])
    return sum


sum = 0
for i in range(1, 1001):
    sum = sum + sum_digit(i)

print(sum)
