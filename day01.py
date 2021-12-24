# Part 1 ----------------------------------------
with open("input.txt", "r") as file:
    nums = list(map(int, file.read().splitlines()))

count = 0
for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        count += 1
print(count)


# Part 2 ----------------------------------------
count = 0
sliding_sums = []
for start_idx in range(0, len(nums)-2):
    sliding_sum = sum(nums[start_idx:start_idx+3])
    sliding_sums.append(sliding_sum)
    if start_idx > 0 and sliding_sums[start_idx] > sliding_sums[start_idx - 1]:
        count += 1
print(count)
