def main():
    with(open("./input.txt", "r")) as fp:
        lines = map(str.strip, fp.readlines())

    total = 0
    for line in lines:
        digits = list(map(int,list(line)))
        found_max = 0

        for digit_ix, digit_1 in enumerate(digits):
            remainder_digits = digits[digit_ix+1:]
            for digit_2 in remainder_digits:
                built_num = int(str(digit_1) + str(digit_2))
                if built_num > found_max:
                    found_max = built_num

        total += found_max
    print(f"total: {total}")

if __name__ == "__main__":
    main()