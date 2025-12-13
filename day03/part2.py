from collections import deque
def main():
    with(open("./input.txt", "r")) as fp:
        lines = map(str.strip, fp.readlines())

    # sort-of monotonic stack time
    # monotonic stack maintains an ordering by popping items from the stack when the rule is violated
    # in our case we have the fun extra restriction that we must also throw away exactly m digits of the n digit number
    # where m = len(n) - 12
    # in the example the numbers are 15 digits, we must end up with 12, so we must throw away exactly 3 digits
    # or put another way, we may only apply the monotonic stack properties while we still have stack pops remaining
    # then we just have to append the remaining digits to maintain the required final length.
    # Finally just chop the first 12 digits from the stack to build the number those will be the highest in-order
    # numbers, followed by whatever was left in the lower-worth places.

    # unconditionally push first item
    # for remaining digits
    # while stack has items and current digit is greater that last digit AND we have pops left
    #  pop last digit, decrement pop counter
    # unconditionally push current digit
    # once all digits consumed, return the first n digits of the stack)

    total = 0
    digit_length_to_find = 12
    for line in lines:
        pops_remaining = len(line) - digit_length_to_find
        stack = []
        digits = deque(map(int,list(line)))
        stack.append(digits[0])
        digits.popleft()

        while len(digits) > 0:
            current_digit = digits.popleft()

            while (len(stack) > 0 and current_digit > stack[-1] and pops_remaining > 0):
                stack.pop()
                pops_remaining -= 1
            
            stack.append(current_digit)

        total += int(str.join("", map(str,stack[:digit_length_to_find])))

    print(f"total: {total}")

if __name__ == "__main__":
    main()