lists = [1,3,5,2,2]

seen = set()
duplicate = set()

for i in lists:
  if i in seen:
    duplicate.add(i)
  else:
    seen.add(i)

print(duplicate)