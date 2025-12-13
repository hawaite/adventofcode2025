from dataclasses import dataclass
from enum import Enum

@dataclass(frozen=True)
class Point:
    row: int
    col: int

class Direction(Enum):
    UP =            Point(-1, 0)
    UP_RIGHT =      Point(-1, 1)
    RIGHT =         Point(0, 1)
    DOWN_RIGHT =    Point(1, 1)
    DOWN =          Point(1, 0)
    DOWN_LEFT =     Point(1, -1)
    LEFT =          Point(0, -1)
    UP_LEFT =       Point(-1, -1)

class Grid:
    def __init__(self, gridDef:list[str]):
        self.width = len(gridDef[0].strip())
        self.height = len(gridDef)
        self.grid_data = []
        for row in gridDef:
            self.grid_data.append(list(row.strip()))

    def get_point(self, point):
        return self.grid_data[point.row][point.col]
    
    def set_point(self, point, value):
        self.grid_data[point.row][point.col] = value

    # return value OR return None if point it out of bounds
    def get_value_in_direction_or_none(self, point:Point, direction:Direction):
        target_row = point.row + direction.value.row
        target_col = point.col + direction.value.col
        if target_row < 0 or target_col < 0 or target_row >= (self.height) or target_col >= (self.width):
            return None
        return self.get_point(Point(target_row, target_col))

    def print_grid(self):
        for row in self.grid_data:
            print(row)
    
    def __repr__(self):
        return f"<Grid: width={self.width}, height={self.height}>"
