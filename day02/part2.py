def get_divisors(num):
    divisors = []
    for i in range(1, (num//2) + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def main():
    with(open("./input.txt", "r")) as fp:
        line = fp.readline().strip()

    # for the length of the string
    # get all divisors of the length of the string because repeating part must have length of a divisor
    # for each divisor, grab that number of chars from the start, build string out to full length, and then compare to original string
    
    total = 0
    ranges = line.split(",")
    for r in ranges:
        start, end = r.split("-")
        for i in range(int(start), int(end)+1):
            i_str = str(i)
            for divisor in get_divisors(len(i_str)):
                test_str = i_str[:divisor] * (len(i_str)//divisor)
                if i_str == test_str:
                    total += i
                    break # only count once

    print(f"total: {total}")

if __name__ == "__main__":
    main()