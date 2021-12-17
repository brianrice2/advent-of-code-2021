from collections import Counter


# Part 1 ----------------------------------------
with open('input1.txt', 'r') as file:
    data = file.read().splitlines()

gamma = ''
eps = ''
for bit in range(len(data[0])):
    counts = Counter([x[bit] for x in data])
    most_freq = max(counts, key=counts.get)
    least_freq = min(counts, key=counts.get)
    gamma += most_freq
    eps += least_freq

gamma = int(gamma, 2)
eps = int(eps, 2)
print(f'Part 1: {gamma * eps}')


# Part 2 ----------------------------------------
with open('input1.txt', 'r') as file:
    data = file.read().splitlines()

bit = 0
nums = data
while bit < len(data[0]):
    print('bit', bit, 'nums', nums)
    counts = Counter([x[bit] for x in nums])
    print('counts', counts)
    most_freq = max(counts, key=counts.get)
    least_freq = min(counts, key=counts.get)

    if most_freq == least_freq:
        most_freq = '1'
    
    nums = [x for x in nums if x[bit] == most_freq]

    if len(nums) == 1:
        oxy = nums[0]
        print(nums)
        break
    
    bit += 1

bit = 0
nums = data
while bit < len(data[0]):
    counts = Counter([x[bit] for x in nums])
    most_freq = max(counts, key=counts.get)
    least_freq = min(counts, key=counts.get)

    if most_freq == least_freq:
        least_freq = '0'
    
    nums = [x for x in nums if x[bit] == least_freq]

    if len(nums) == 1:
        co2 = nums[0]
        print(nums)
        break
    
    bit += 1

oxy = int(oxy, 2)
co2 = int(co2, 2)
print(f'Part 2: {oxy * co2}')
