t = "Car and car are different?! No, they are the same."

t_lower = t.lower()

punctuations = "!?,.'\""

for p in punctuations:
    t_lower = t_lower.replace(p, "")

print(f"원본: {t}")
print(f"수정 후: {t_lower}")