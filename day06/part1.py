from functools import reduce
import operator

def main():
    with(open("./input.txt", "r")) as fp:
        lines = fp.readlines()

    all_lines = [line.strip().split() for line in lines]

    num_rows = all_lines[:-1]
    operators = all_lines[-1:][0]

    total = 0
    
    for col in range(len(num_rows[0])):
        op = operators[col]
        nums = []
        for row in range(len(num_rows)):
            nums.append(num_rows[row][col])
        if op == "+":
            total += sum(map(int, nums))
        elif op == "*":
            total += reduce(operator.mul, map(int, nums), 1)

    print(f"total: {total}")

if __name__ == "__main__":
    main()