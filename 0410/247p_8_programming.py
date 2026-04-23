def getMoneyText(amount):
    units = ["", "십", "백"]
    nums = ["", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    res = ""
    
    h = amount // 100
    if h > 0: res += nums[h] + "백 "
    
    t = (amount % 100) // 10
    if t > 0: res += nums[t] + "십 "
    
    o = amount % 10
    if o > 0: res += nums[o]
    
    return res + "원"

money = int(input("1000 이하의 금액을 입력하시오: "))
print(getMoneyText(money))