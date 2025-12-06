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
            continue
        str_parts = line.split("-")
        
        if len(str_parts) == 1:
            # its an id
            id = int(str_parts[0])
            for fresh_range in fresh_ranges:
                if id >= fresh_range.start and id <= fresh_range.end:
                    total += 1
                    break # bail after first match
        else:
            # its a range
            fresh_ranges.append(Range(int(str_parts[0]), int(str_parts[1])))

    print(f"total: {total}")
    

if __name__ == "__main__":
    main()