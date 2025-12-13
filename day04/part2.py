from grid import Grid, Direction, Point

def main():
    with(open("./input.txt", "r")) as fp:
        lines = fp.readlines()
    
    parsed_grid = Grid(lines)
    total = 0
    made_change = True

    # mild optimization: Only iterate over the points we know have paper rolls in them
    # instead of iterating the whole grid.
    paper_points = []
    for row in range(parsed_grid.height):
        for col in range(parsed_grid.width):
            p = Point(row, col)
            if parsed_grid.get_point(p) == "@":
                paper_points.append(p)

    while made_change:
        made_change = False
        remaining_paper_points = []
        for p in paper_points:
            surrounding_cell_values = [parsed_grid.get_value_in_direction_or_none(p, dir) for dir in Direction]
            surrounding_roll_count = sum(1 for x in surrounding_cell_values if x == "@")
            if surrounding_roll_count < 4:
                total += 1
                parsed_grid.set_point(p, ".")
                made_change = True
            else:
                remaining_paper_points.append(p)
        paper_points = remaining_paper_points

    print(f"total: {total}")


if __name__ == "__main__":
    main()