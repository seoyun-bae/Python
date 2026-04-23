def sort_numbers(n1, n2):
    if n1 > n2:
        return n2, n1
    else:
        return n1, n2


num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

low, high = sort_numbers(num1, num2)

print(f"결과: 작은 값은 {low}, 큰 값은 {high}입니다.")