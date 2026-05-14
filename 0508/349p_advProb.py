phrase = input("문자열을 입력하시오: ")
acronym = ""

stop_words = ["by", "in", "the", "of"]


for word in phrase.split():
    
    if word.lower() not in stop_words:
        
        acronym += word[0].upper()

print(f"결과: {acronym}")