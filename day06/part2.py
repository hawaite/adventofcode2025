from functools import reduce
import operator

def add(num_list):
    return sum(num_list)

def mult(num_list):
    return reduce(operator.mul, num_list, 1)

def main():
    with(open("./input.txt", "r")) as fp:
        lines = fp.readlines()
    total = 0

    num_lines = []
    ops = lines[-1].split()
    for line in lines[:-1]:
        num_lines.append(line.strip("\n")+" ")

    print(num_lines)
    print(ops)


    current_group_nums = []
    for col in range(len(num_lines[0])):
        col_chars = []
        for row in range(len(num_lines)):
            col_chars.append(num_lines[row][col])

        any_non_blank = any(filter(lambda x: x != " ", col_chars))
        all_blank = not any_non_blank
        if not all_blank:
            current_group_nums.append(int(str.join("", col_chars).strip()))
        else:
            print(current_group_nums)
            print(ops[0])
            if ops[0] == "+":
                res = add(current_group_nums)
                print(res)
                total += res
            elif ops[0] == "*":
                res = mult(current_group_nums)
                print(res)
                total += res
            print("---------")
            # pop an op
            ops = ops[1:]
            current_group_nums = []
            # was all blank.
            # do op on the group
            # reset current_group
        # print(f"col: {col}, chars: {col_chars} all_blank: {not any_non_blank}")


    print(f"total: {total}")

if __name__ == "__main__":
    main()