from dataclasses import dataclass

@dataclass
class Range:
    start:  int
    end:    int

def main():
    with(open("./input.txt", "r")) as fp:
        lines = fp.readlines()

    total = 0
    fresh_ranges: list[Range] = []
    for line in map(str.strip, lines):
        if line == "":
            break 
        start, end = line.split("-")
        fresh_ranges.append(Range(int(start), int(end)))

    fresh_ranges = sorted(fresh_ranges, key=lambda x: x.start)

    consolidated_ranges = []
    made_change = True

    while made_change:
        made_change = False
        while len(fresh_ranges) > 0:
            if len(fresh_ranges) >= 2:
                first = fresh_ranges[0]
                second = fresh_ranges[1]

                # test for overlap OR adjacent ranges
                if (first.start <= second.start and first.end >= second.start) or first.end == (second.start - 1):
                    # found overlap. build and store combined range then remove both parts from the range list
                    consolidated_range = Range(min(first.start, second.start), max(first.end, second.end))
                    consolidated_ranges.append(consolidated_range)
                    fresh_ranges = fresh_ranges[2:] # chop first two as consumed
                    made_change = True
                else:
                     # not an overlap. move this range to the consolidated ranges list and remove from original list
                    consolidated_ranges.append(fresh_ranges[0])
                    fresh_ranges = fresh_ranges[1:]
            else: # only 1 left. Add it to output list
                consolidated_ranges.append(fresh_ranges[0])
                fresh_ranges = []

        # copy the consolidated ranges back to the original list
        fresh_ranges = consolidated_ranges
        consolidated_ranges = []

    # add 1 to make the total inclusive of both range ends
    total = sum([(x.end - x.start)+1 for x in fresh_ranges])

    print(f"total: {total}")
if __name__ == "__main__":
    main()