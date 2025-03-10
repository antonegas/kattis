"""
author: Anton Nilsson
testcase 1:
in:
2
d5
a1

out:
4 b7 f7 b3 f3 h1
6 h8

"""

from collections import deque

def get_hiding_places(chess_position: str) -> list[str]:
    column_letters = "abcdefgh"
    column = column_letters.index(chess_position[0])
    row = int(chess_position[1]) - 1

    board = [[-1] * 8 for _ in range(8)]
    board[row][column] = 0

    queue = deque([(column, row, 0)])

    while len(queue) > 0:
        x, y, turn = queue.popleft()

        for dx, dy in [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]:
            if x + dx < 0 or x + dx > 7 or y + dy < 0 or y + dy > 7:
                continue

            if board[y + dy][x + dx] >= 0:
                continue

            board[y + dy][x + dx] = turn + 1

            queue.append((x + dx, y + dy, turn + 1))

    result = list()
    most_moves = 0

    for y in reversed(range(8)):
        for x in range(8):
            chess_notation = f"{column_letters[x]}{y + 1}"
            if board[y][x] > most_moves:
                most_moves = board[y][x]
                result = [chess_notation]
            elif board[y][x] == most_moves:
                result.append(chess_notation)

    return most_moves, result

if __name__ == "__main__":
    output = list()
    lines = open(0, "r").read().splitlines()[1:]

    index = 0

    while index < len(lines):
        chess_position = lines[index]

        turns, hiding_places = get_hiding_places(chess_position)

        output.append(str(turns) + " " + " ".join(hiding_places))

        index += 1

    open(1, "w").write("\n".join(output))