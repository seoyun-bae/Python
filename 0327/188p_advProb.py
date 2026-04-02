number = 2

while number < 100:
    divisor = 2
    prime = True

    while divisor < number:
        if number % divisor == 0:
            prime = False
            break
        divisor += 1
    if prime:
        print(number, end=" ")

    number += 1
