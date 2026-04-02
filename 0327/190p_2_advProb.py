divisor = 1.0
dividend = 4.0
total_sum = 0.0
loop_count = int(input("반복 횟수를 입력하세요: "))
for i in range(loop_count):
    total_sum += dividend / divisor
    divisor += 2.0
    dividend *= -1.0
print(f"Pi = {total_sum:f}")

# for문. 정해진 횟수로 실행되기 때문