def main():
    with(open("./input.txt", "r")) as fp:
        lines = fp.readlines()

    processed = []
    total_splits = 0
    for line_ix, line in enumerate(lines):
        line_as_list = list(line.strip())
        # move first line to output unconditionally
        if line_ix == 0:
            processed.append(line_as_list)
            continue
        
        # otherwise, iterate cells and apply rules based on previous row
        prev_row = processed[-1]
        for cell_ix, cell in enumerate(line_as_list):
            # if cell above is a pipe or an S, replace current cell with a beam
            if cell == "." and prev_row[cell_ix] in ["|", "S"]:
                line_as_list[cell_ix] = "|"
            # if a cell is a splitter with a beam above, split it
            elif cell == "^" and prev_row[cell_ix] == "|":
                line_as_list[cell_ix-1] = "|"
                line_as_list[cell_ix+1] = "|"
                total_splits += 1
        processed.append(line_as_list)

    print(f"total: {total_splits}")
        

if __name__ == "__main__":
    main()