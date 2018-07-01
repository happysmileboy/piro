number = [2, 4, 6, 8, 10, 12, 14]


for i in range(len(number)): #index 0 to 7
    if i >= len(number) - 1 - i:
        break

    temp = number[i]
    number[i] = number[(len(number) - 1) - i] #7 - i
    number[(len(number) - 1) - i] = temp


print("뒤집어진 리스트: " + str(number))