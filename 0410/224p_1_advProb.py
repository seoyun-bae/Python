def weeklyPay(hours, rate=10000):
    if hours > 30:
        money = rate * 30 + 1.5 * rate * (hours - 30)
    else:
        money = rate * hours
    return money