def weeklyPay(hours, rate=10000):
    if hours > 30:
        money = rate * 30 + 1.5 * rate * (hours - 30)
    else:
        money = rate * hours
    return money


r = int(input("시급을 입력하세요: "))
h = int(input("근무 시간을 입력하세요: "))

result = weeklyPay(hours=h, rate=r)

print(f"주급은 {result}원입니다.")