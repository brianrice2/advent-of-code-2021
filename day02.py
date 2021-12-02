with open("input1.txt", "r") as file:
    commands = file.read().splitlines()


# Part 1
depth = 0
horizontal = 0
for line in commands:
    move, howmany = line.split()
    howmany = int(howmany)

    if move == 'forward':
        horizontal += howmany
    elif move == 'down':
        depth += howmany
    elif move == 'up':
        depth -= howmany
        depth = max(0, depth)  # Don't have negative depth
print(depth * horizontal)


# Part 2
with open("input1.txt", "r") as file:
    commands = file.read().splitlines()

depth, horizontal, aim = 0, 0, 0
for line in commands:
    move, howmany = line.split()
    howmany = int(howmany)

    if move == 'forward':
        horizontal += howmany
        depth += aim * howmany
        depth = max(0, depth)  # Don't have negative depth
    elif move == 'down':
        aim += howmany
    elif move == 'up':
        aim -= howmany
print(depth, horizontal, aim, '=', depth * horizontal)
