n = int(input("정수를 입력하시오: "))

if n % 3 == 0 and n % 5 == 0:
    print("Python Express")
elif n % 3 == 0:
    print("Python")
elif n % 5 == 0:
    print("Express")