def main():
    current_digit = 50
    zero_passings = 0
    
    with(open("./input.txt", "r")) as fp:
        lines = fp.readlines()
        for line in lines:
            
            dir = line[0]
            direction_operation = int.__sub__ if dir == "L" else int.__add__
            magnitude = int(line[1:])
            
            # work out the number of full laps that we can get out of the magnitude given
            full_laps, remainder = divmod(magnitude, 100)
            zero_passings += full_laps

            #perform remaining move
            prev_digit = current_digit
            current_digit = direction_operation(current_digit, remainder) % 100

            # landed on 0. Count this as another zero passing and make sure not to count it again.
            if current_digit == 0:
                zero_passings += 1
                continue

            # if turning left (numbers going down) and the new number is suddenly higher
            # and we werent previously on 0 because that has already been counted
            if dir == "L" and current_digit > prev_digit and prev_digit != 0:
                zero_passings += 1
            # if turning right (numbers going up) and the new number is suddenly lower
            # and we werent previously on 0 because that has already been counted
            elif dir == "R" and current_digit < prev_digit and prev_digit != 0:
                zero_passings += 1
            
            

    print("Zero passings: ", zero_passings)

if __name__ == "__main__":
    main()