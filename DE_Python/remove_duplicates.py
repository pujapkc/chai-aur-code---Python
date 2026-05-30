lst = [1, 2, 3, 2, 4, 1, 5]

seen = set()
result = []

for num in lst:
    if num not in result:
        # seen.add(num)
        result.append(num)

print(result)