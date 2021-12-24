from collections import Counter
from typing import Dict


DAYS = 256

def time_step(age_dict: Dict, newborn_age: int = 8, reset_age: int = 6) -> None:
    zeros = age_dict.get(0, 0)
    for age in range(newborn_age):
        age_dict[age] = age_dict.get(age+1, 0)

    # Each day, a 0 becomes a 6 and adds a new 8 to the end of the list
    age_dict[reset_age] = age_dict.get(reset_age, 0) + zeros
    age_dict[newborn_age] = zeros
    return None


def pass_time(age_dict: Dict, days: int) -> None:
    for _ in range(days):
        time_step(age_dict)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        fishes = map(int, file.read().strip().split(','))

    fish_ages = Counter(fishes)
    pass_time(fish_ages, DAYS)
    print(f'Number of lanternfish: {sum(fish_ages.values())}')
