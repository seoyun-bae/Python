def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n - 1)


num = int(input("어디까지 더할까요?: "))
print(f"1부터 {num}까지의 합은 {sum_recursive(num)}입니다.")