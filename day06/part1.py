from functools import reduce
import operator

def add(num_list):
    return sum(map(int, num_list))

def mult(num_list):
    return reduce(operator.mul, map(int, num_list), 1)

def main():
    with(open("./input.txt", "r")) as fp:
        lines = fp.readlines()

    all_lines = []
    for line in lines:
        line_parts = line.strip().split()
        all_lines.append(line_parts)

    num_rows = all_lines[:-1]
    operator_row = all_lines[-1:][0]

    print(num_rows)
    print(operator_row)
    total = 0
    
    for col in range(len(num_rows[0])):
        op = operator_row[col]
        nums = []
        for row in range(len(num_rows)):
            nums.append(num_rows[row][col])
        print(nums)
        print(op)
        if op == "+":
            print(add(nums))
            total += add(nums)
        if op == "*":
            print(mult(nums))
            total += mult(nums)
        print("--------------------")

    print(f"total: {total}")

if __name__ == "__main__":
    main()