from math import ceil, inf
from statistics import mean, median
from typing import List, Tuple


def get_total_travel(positions: List, align_at: int) -> int:
    return sum(map(lambda x: abs(x - align_at), positions))


def get_special_travel(positions: List, align_at: int) -> int:
    def special_dist(current: int, target: int) -> int:
        diff = abs(current - target) + 1
        return diff * (diff - 1) / 2
    return sum(map(lambda x: special_dist(x, align_at), positions))


def minimize_special_travel(positions: List) -> Tuple[int, int]:
    avg = mean(positions)
    med = round(median(positions), 0)
    start, end = int(min(avg, med)), int(ceil(max(avg, med)))

    best_candidate = -1
    min_travel = inf
    for candidate in range(start, end+1):
        dist = get_special_travel(positions, candidate)
        if dist < min_travel:
            min_travel = dist
            best_candidate = candidate
    
    return min_travel, best_candidate


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        positions = list(map(int, file.read().strip().split(',')))
    travel = get_total_travel(positions, round(median(positions), 0))
    print(f'Part 1: {int(travel)}')

    special_dist, special_location = minimize_special_travel(positions)
    print(f'Part 2: {int(special_dist)} (at loc {special_location})')
