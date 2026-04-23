def get_gcd(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

n1 = int(input("첫 번째 정수: "))
n2 = int(input("두 번째 정수: "))
print(get_gcd(n1, n2))