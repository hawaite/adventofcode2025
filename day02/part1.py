def main():
    with(open("./input.txt", "r")) as fp:
        line = fp.readline().strip()
    
    total = 0
    ranges = line.split(",")
    for r in ranges:
        start, end = r.split("-")
        for i in range(int(start), int(end)+1):
            id_str = str(i)
            if len(id_str) % 2 == 0:
                # only even lengths can match
                half_one = id_str[:len(id_str)//2]
                half_two = id_str[len(id_str)//2:]
                if half_one == half_two:
                    total += i

    print(f"total: {total}")


if __name__ == "__main__":
    main()