from bisect import bisect_left, bisect_right


def read_ints():
    return list(map(int, input().split()))


def solve_one_case():
    n, m, q = read_ints()
    grid = [input().strip() for _ in range(n)]
    moves = input().strip()

    a_cells = []
    b_cells = []

    for row in range(n):
        line = grid[row]
        for col in range(m):
            ch = line[col]
            if ch == 'A':
                a_cells.append((row, col))
            elif ch == 'B':
                b_cells.append((row, col))

    y_to_xs = {}
    x_to_ys = {}

    for ax, ay in a_cells:
        for bx, by in b_cells:
            dx = ax - bx
            dy = ay - by
            y_to_xs.setdefault(dy, []).append(dx)
            x_to_ys.setdefault(dx, []).append(dy)

    for dy, xs in y_to_xs.items():
        xs.sort()
    for dx, ys in x_to_ys.items():
        ys.sort()

    sx = 0
    sy = 0

    for move in moves:
        if move == 'N':
            xs = y_to_xs.get(sy, [])
            idx = bisect_left(xs, sx)
            if idx == 0:
                return True
            sx = xs[idx - 1] + 1
        elif move == 'S':
            xs = y_to_xs.get(sy, [])
            idx = bisect_right(xs, sx)
            if idx == len(xs):
                return True
            sx = xs[idx] - 1
        elif move == 'W':
            ys = x_to_ys.get(sx, [])
            idx = bisect_left(ys, sy)
            if idx == 0:
                return True
            sy = ys[idx - 1] + 1
        else:
            ys = x_to_ys.get(sx, [])
            idx = bisect_right(ys, sy)
            if idx == len(ys):
                return True
            sy = ys[idx] - 1

    return False


t = int(input())
out_lines = []
for _ in range(t):
    out_lines.append('TAK' if solve_one_case() else 'NIE')
print('\n'.join(out_lines))