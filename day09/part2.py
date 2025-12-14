from itertools import combinations
from shapely import Polygon

def main():
    with(open("./input.txt", "r")) as fp:
        lines = list(map(str.strip, fp.readlines()))

    max_area = 0
    polygon_points = []
    # add first point to the end to close the polygon
    lines.append(lines[0])
    for point in lines:
        p_a, p_b = map(int, point.split(","))
        polygon_points.append((p_a, p_b))

    polygon = Polygon(polygon_points)

    for p1, p2 in combinations(lines, 2):
        p1_a, p1_b = map(int, p1.split(","))
        p2_a, p2_b = map(int, p2.split(","))
        area = (abs(p1_a - p2_a) + 1) * (abs(p1_b - p2_b) + 1) 

        rectangle = Polygon([(p1_a, p1_b), (p1_a, p2_b), (p2_a, p2_b), (p2_a, p1_b), (p1_a, p1_b)])
        
        if polygon.contains(rectangle):
            max_area = max(max_area, area)
        
    print(f"max: {max_area}")

if __name__ == "__main__":
    main()