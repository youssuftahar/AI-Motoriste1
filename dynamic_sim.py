from grid import START, GOAL, GRID
from astar import get_next_step
from simulator import render

class Car:
    def __init__(self):
        self.pos = list(START)
        self.path = []
        self.step = 0

    def sense(self, grid):
        """محاكاة حساسات بسيطة"""
        x, y = self.pos
        obstacles = []

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny] == 1:
                        obstacles.append((nx, ny))
        return obstacles

    def replan(self):
        """إعادة حساب المسار"""
        self.path = get_next_step(tuple(self.pos), GOAL)

    def move(self):
        if not self.path:
            self.replan()

        if self.step < len(self.path):
            self.pos = list(self.path[self.step])
            self.step += 1


def run():
    car = Car()

    for i in range(50):
        print(f"\nStep {i} -> {car.pos}")

        car.move()

        render(car.pos)

        # إعادة تخطيط عند الحاجة
        if i % 5 == 0:
            car.replan()


if __name__ == "__main__":
    print("DYNAMIC SIM STARTED")
    run()
