import time
import os

GRID_SIZE = 5
DIRECTIONS = ["N", "E", "S", "W"]
DIR_SYMBOLS = {"N": "↑", "E": "→", "S": "↓", "W": "←"}

class Robot:
    def __init__(self, x, y, direction="N"):
        self.x = x
        self.y = y
        self.direction = direction

    def turn_left(self):
        idx = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(idx - 1) % 4]

    def turn_right(self):
        idx = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(idx + 1) % 4]

    def move(self):
        if self.direction == "N" and self.y > 0:
            self.y -= 1
        elif self.direction == "S" and self.y < GRID_SIZE - 1:
            self.y += 1
        elif self.direction == "E" and self.x < GRID_SIZE - 1:
            self.x += 1
        elif self.direction == "W" and self.x > 0:
            self.x -= 1

def print_grid(robot):
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(GRID_SIZE):
        row = ""
        for x in range(GRID_SIZE):
            if robot.x == x and robot.y == y:
                row += DIR_SYMBOLS[robot.direction] + " "
            else:
                row += ". "
        print(row)
    print("\n")
    time.sleep(0.3)

r = Robot(0, 0, "N")

for _ in range(4):
    for _ in range(GRID_SIZE - 1):
        r.move()
        print_grid(r)
    r.turn_right()
    print_grid(r)

print("Robot finished the square path!")
