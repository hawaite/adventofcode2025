from functools import reduce
import operator

def main():
    with(open("./input.txt", "r")) as fp:
        lines = fp.readlines()
    
    total = 0

    ops = lines[-1].split()
    # update all the number lines to not finish in a newline, 
    # but add an extra space on the end of every line such that
    # we catch the last block of numbers
    number_lines = [x.strip("\n") + " " for x in lines[:-1]]
    total_col_count = len(number_lines[0])
    number_of_lines = len(number_lines)

    current_group_nums = []
    for col in range(total_col_count):
        col_chars = [ number_lines[row_ix][col] for row_ix in range(number_of_lines) ]

        all_blank = not any(filter(lambda x: x != " ", col_chars))

        if not all_blank: # glue this number together and store it
            current_group_nums.append(int(str.join("", col_chars).strip()))
        else: # column was blank, process current group
            if ops[0] == "+":
                total += sum(current_group_nums)
            elif ops[0] == "*":
                total += reduce(operator.mul, current_group_nums, 1)
            # remove used operator and empty the current group
            ops = ops[1:]
            current_group_nums = []

    print(f"total: {total}")

if __name__ == "__main__":
    main()