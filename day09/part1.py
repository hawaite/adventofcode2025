from itertools import combinations

def main():
    with(open("./input.txt", "r")) as fp:
        lines = list(map(str.strip, fp.readlines()))

    max_area = 0
    for p1, p2 in combinations(lines, 2):
        p1_a, p1_b = map(int, p1.split(","))
        p2_a, p2_b = map(int, p2.split(","))
        area = (abs(p1_a - p2_a) + 1) * (abs(p1_b - p2_b) + 1) 
        max_area = max(max_area, area)
        
    print(f"max: {max_area}")

if __name__ == "__main__":
    main()