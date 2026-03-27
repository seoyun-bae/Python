a = float(input("a를 입력하세요: "))
b = float(input("b를 입력하세요: "))
c = float(input("c를 입력하세요: "))

D = (b**2) - (4*a*c)

if D > 0:
    r1 = (-b + D**0.5) / (2 * a)
    r2 = (-b - D**0.5) / (2 * a)
    print(f"실근은{r1}과 {r2}입니다.")
elif D == 0:
    r = -b / (2 * a)
    print(f"중근은 {r}입니다.")
else:
    print("실근이 존재하지 않습니다.")
