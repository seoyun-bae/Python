text = input("문자열을 입력하시오: ")
forbidden = input("금지할 글자를 입력하시오: ").split()
for word in forbidden:
    text = text.replace(word, "*"*len(word))
print(text)