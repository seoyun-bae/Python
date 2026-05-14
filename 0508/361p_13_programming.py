s = input("문자열을 입력하시오: ")
letters = sum(1 for c in s if c.isalpha())
digits = sum(1 for c in s if c.isdigit())
print(f"-> {{ \"LETTERS\": {letters}, \"DIGITS\": {digits} }}")