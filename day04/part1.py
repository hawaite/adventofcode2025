from grid import Grid, Direction, Point

def main():
    with(open("./input.txt", "r")) as fp:
        lines = fp.readlines()
    
    parsed_grid = Grid(lines)
    total = 0
    
    for row in range(parsed_grid.height):
        for col in range(parsed_grid.width):
            p = Point(row, col)
            if parsed_grid.get_point(p) == "@":
                surrounding_cell_values = [parsed_grid.get_value_in_direction_or_none(p, dir) for dir in Direction]
                surrounding_roll_count = sum(1 for x in surrounding_cell_values if x == "@")
                if surrounding_roll_count < 4:
                    total += 1

    print(f"total: {total}")


if __name__ == "__main__":
    main()