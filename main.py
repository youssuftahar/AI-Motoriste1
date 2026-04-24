from grid import START, GOAL
from simulator import render
from astar import get_next_step

pos = START

for step in range(100):

    if pos == GOAL:
        print("🎯 وصلت السيارة للهدف")
        break

    next_pos = get_next_step(pos)

    if next_pos is None:
        print("❌ لا يوجد مسار")
        break

    pos = next_pos

    print(f"Step {step} -> {pos}")
    render(pos)
