t = "That is a shit movie. What a shit ending!"
forbidden_word = "shit"

word_count = t.count(forbidden_word)

clean_message = t.replace(forbidden_word, "***") # 완전히 지우려면 "" 로 변경

print(f"원본 메시지: {t}")
print(f"금지어 '{forbidden_word}' 사용 횟수: {word_count}")
print(f"필터링된 메시지: {clean_message}")