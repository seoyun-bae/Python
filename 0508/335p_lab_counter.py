text_data ="Create the highest, grandest vision posible for your life, because you become what you believe."

word_dic = {}
for w in text_data.split():
    if w in word_dic:
        word_dic[w] += 1
    else:
        word_dic[w] = 1

for w, count in sorted(word_dic.items()):
    print(w, "의 등장횟수=", count)