nums = [1,2,2,3,4,5,5] # remove duplicates

unique = []

for num in nums:
    if num not in unique:
        unique.append(num)

# print(unique)

unique = list(dict.fromkeys(nums))
print(unique)
