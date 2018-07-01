def mask_security_number(security_number):
    #스트링으로 받고 문자열로 바꾼다.
    list_number = list(security_number)
    #문자열의 끝 4개를 반복문으로 *로 바꾼다.
    for i in range(len(list_number)):# 0 ~ 13
        list_number[(len(list_number) - 1 - i)] = '*'
        if i > 2:
            break
    #리스트를 다시 스트링으로 바꾼다.
    result = ""
    for i in list_number:
        result = result + i

    return result


print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))