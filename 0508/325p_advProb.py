txt = input("작문 리포트 입력: ")
words = txt.split()

total = len(words)
unique = len(set(words))

ratio = (unique / total) if total else 0

print(f"\n전체 단어: {total}개 | 고유 단어: {unique}개 | 비율: {ratio * 100:.1f}%")

print("결과: 학점 A" if ratio > 0.5 else "결과: 학점 B 이하")