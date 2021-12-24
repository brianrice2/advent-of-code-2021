import numpy as np


# Part 1 ----------------------------------------
# Parse the input draws and boards
with open('input1.txt', 'r') as file:
    data = file.read().split('\n\n')
draws = map(int, data[0].split(','))
boards = []
for raw_board in data[1:]:
    rows = raw_board.split('\n')
    board = [list(map(int, row.split())) for row in rows]
    boards.append(board)
boards = np.array(boards)
tracker = np.ones(boards.shape, dtype=np.int32)

def update_tracker(boards, tracker, draw):
    tracker = np.where(boards == draw, 0, tracker)
    return tracker

def find_winner(tracker):
    for board_idx in range(tracker.shape[0]):
        board = tracker[board_idx]
        if any(np.sum(board, axis=0) == 0) or any(np.sum(board, axis=1) == 0):
            return board_idx
    return None

for draw in draws:
    tracker = update_tracker(boards, tracker, draw)
    winning_board = find_winner(tracker)
    if winning_board:
        score = np.sum(boards[winning_board] * tracker[winning_board])
        score *= draw
        break

print(f'Part 1: {score}')


# Part 2 ----------------------------------------
with open('input1.txt', 'r') as file:
    data = file.read().split('\n\n')
draws = list(map(int, data[0].split(',')))
boards = []
for raw_board in data[1:]:
    rows = raw_board.split('\n')
    board = [list(map(int, row.split())) for row in rows]
    boards.append(board)
boards = np.array(boards)
tracker = np.ones(boards.shape, dtype=np.int32)

def find_winners(tracker):
    winners = set()
    for board_idx in range(tracker.shape[0]):
        board = tracker[board_idx]
        if any(np.sum(board, axis=0) == 0) or any(np.sum(board, axis=1) == 0):
            winners.add(board_idx)
    return winners

winning_boards = set()
winning_scores = []
for draw in draws:
    tracker = update_tracker(boards, tracker, draw)
    winners = find_winners(tracker)
    for winning_board in winners:
        if winning_board not in winning_boards:
            winning_boards.add(winning_board)
            score = np.sum(boards[winning_board] * tracker[winning_board])
            score *= draw
            winning_scores.append(score)

print(f'Part 2: {winning_scores[-1]}')
