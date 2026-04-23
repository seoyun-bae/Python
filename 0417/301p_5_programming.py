words = ['aba', 'xyz', 'abc', '121']
count = 0

for w in words:
    if len(w) > 0 and w[0] == w[-1]:
        count += 1

print(words)
print(f"문자열의 개수 = {count}")