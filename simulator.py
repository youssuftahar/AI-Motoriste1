from grid import grid, GOAL

def render(car_pos):
    for i in range(10):
        row = ""
        for j in range(10):
            if (i, j) == car_pos:
                row += "🚗 "
            elif (i, j) == GOAL:
                row += "🏁 "
            elif grid[i][j] == 1:
                row += "🟫 "
            else:
                row += "⬜ "
        print(row)
    print()
