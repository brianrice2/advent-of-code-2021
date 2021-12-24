import numpy as np


# Part 1 ----------------------------------------
with open('input1.txt', 'r') as file:
    data = file.read().splitlines()

DIAGRAM_SIZE = 1000
diagram = np.zeros((DIAGRAM_SIZE, DIAGRAM_SIZE), dtype=np.int32)
for line in data:
    start, end = line.split(' -> ')
    start_x, start_y = tuple(map(int, start.split(',')))
    end_x, end_y = tuple(map(int, end.split(',')))
    x_steps, y_steps = abs(end_x - start_x), abs(end_y - start_y)
    x_step = (end_x - start_x) // x_steps if x_steps > 0 else 0
    y_step = (end_y - start_y) // y_steps if y_steps > 0 else 0

    # Skip diagonal lines for Part 1
    # if x_steps > 0 and y_steps > 0:
    #     continue
    
    x = start_x
    y = start_y
    for step in range(max(x_steps, y_steps) + 1):
        diagram[x, y] += 1
        x += x_step
        y += y_step

print(diagram.T)
n_points = np.sum(diagram >= 2)

print(f'Number of overlapping points: {n_points}')
