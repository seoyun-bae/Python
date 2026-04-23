def weeklyPay(rate, hours):
    money = 0
    if (hours > 30):
        money = rate*30 + 1.5*rate*(hours-30)
    else:
        money = rate*hours
    return money


rate = int(input("시급을 입력하세요: "))
hours = int(input("근무 시간을 입력하세요: "))
print("주급은 "+str(weeklyPay(rate,hours)))