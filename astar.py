import heapq
from grid import grid

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(start, goal):
    pq = []
    heapq.heappush(pq, (0, start))

    came_from = {}
    cost = {start: 0}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            break

        x, y = current

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy

            if 0 <= nx < 10 and 0 <= ny < 10:
                if grid[nx][ny] == 1:
                    continue

                new_cost = cost[current] + 1

                if (nx,ny) not in cost or new_cost < cost[(nx,ny)]:
                    cost[(nx,ny)] = new_cost
                    priority = new_cost + heuristic((nx,ny), goal)
                    heapq.heappush(pq, (priority, (nx,ny)))
                    came_from[(nx,ny)] = current

    path = []
    node = goal
    while node != start:
        path.append(node)
        node = came_from[node]
    path.append(start)
    path.reverse()

    return path
