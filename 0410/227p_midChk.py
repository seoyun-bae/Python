def addsub(x, y):
    sum_val = x + y
    sub_val = x - y
    return sum_val, sub_val


result_add, result_sub = addsub(10, 5)

print(f"더한 값: {result_add}")
print(f"뺀 값: {result_sub}")