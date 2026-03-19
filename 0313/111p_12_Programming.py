num = int(input("숫자를 입력하시오: "))
front = num // 1000
back = num % 1000
print(f"{front},{back}")