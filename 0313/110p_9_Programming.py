number = int(input("정수="))

a = number % 10
number = number // 10

b = number % 10
number = number // 10

c = number % 10
number = number // 10

d = number % 10

sum = a + b + c + d
print(sum)