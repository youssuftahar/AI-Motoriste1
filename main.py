from astar import astar
from simulator import run_simulation

start = (0,0)
goal = (9,9)

path = astar(start, goal)

run_simulation(path)

print("Finished successfully")
