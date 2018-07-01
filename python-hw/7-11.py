#빈 리스트 생성
numbers = []

#리스트에 1부터 10까지 넣어준다
i = 0
while i < 10:
    numbers.append(i + 1)
    i += 1
print(numbers)

#리스트에서 홀수만 제거 (중요)
#이 내용 매우 중요! 모든값을 확인하도록 하는 구조!
i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        del numbers[i]
    else:
        i += 1

print(numbers)

#index0 자리에 숫자 20 넣는다
numbers.insert(0, 20)
print(numbers)

numbers.sort()
print(numbers)