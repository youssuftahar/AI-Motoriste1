from grid import grid, GOAL

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_next_step(current):
    x, y = current

    moves = [
        (x+1, y),
        (x-1, y),
        (x, y+1),
        (x, y-1)
    ]

    best = None
    best_score = float("inf")

    for mx, my in moves:
        if 0 <= mx < 10 and 0 <= my < 10:
            if grid[mx][my] == 0:  # ممنوع العوائق
                score = heuristic((mx, my), GOAL)
                if score < best_score:
                    best_score = score
                    best = (mx, my)

    return best
