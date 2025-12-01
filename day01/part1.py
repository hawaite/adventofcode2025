def main():
    current_digit = 50
    zero_landings = 0

    with(open("./input.txt", "r")) as fp:
        lines = fp.readlines()
        for line in lines:
            direction_operation = int.__sub__ if line[0] == "L" else int.__add__
            magnitude = int(line[1:])
            current_digit = direction_operation(current_digit, magnitude) % 100

            if current_digit == 0:
                zero_landings += 1

    print("Zero landings: ", zero_landings)

if __name__ == "__main__":
    main()