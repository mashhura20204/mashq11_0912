# mashq11_0912
#  1-misol

words3 = ["car", "bike", "bus"]
result_14 = [w[::-1] for w in words3]
print(result_14)


# 2-misol

nums3 = [1, 2, 3, 4]
result_15 = [n * 2 for n in nums3]
print(result_15)


# 3-misol

scores = [65, 85, 45, 95, 70]
result_16 = [s for s in scores if s > 70]
print(result_16)


# 4-misol

words4 = ["hello", "123", "world", "456"]
result_17 = [w for w in words4 if w.isalpha()]
print(result_17)


# 5-misol

result_18 = [n for n in range(1, 21) if n % 3 == 1]
print(result_18)

# 6-misol

lst = [1, 2, 3, 4, 5]
result = ["even" if x % 2 == 0 else "odd" for x in lst]
print(result)
