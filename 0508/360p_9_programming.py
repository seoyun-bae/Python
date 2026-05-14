s1 = input("첫 번째 문자열: ")
s2 = input("두 번째 문자열: ")
common = set(s1) & set(s2)
print(f"모두 포함된 글자: {''.join(common)}")