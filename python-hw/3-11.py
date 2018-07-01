def calculate_change(payment, cost):
    change = payment - cost

    fifty_thousand = 50000
    ten_thounsand = 10000
    five_thousand = 5000
    one_thousand = 1000

    fifty_thousand_count = int(change / fifty_thousand)
    change =  change - fifty_thousand * fifty_thousand_count

    ten_thounsand_count = int(change / ten_thounsand)
    change = change - ten_thounsand * ten_thounsand_count

    five_thousand_count = int(change / five_thousand)
    change = change - five_thousand_count*five_thousand

    one_thounsand_count = int(change / one_thousand)

    print("50000원 지폐: %d장" % fifty_thousand_count)
    print("10000원 지폐: %d장" % ten_thounsand_count)
    print("5000원 지폐: %d장" % five_thousand_count)
    print("1000원 지폐: %d장" % one_thounsand_count)


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)