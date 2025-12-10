class Machine:
    target_light_pattern: list[bool]
    current_light_pattern: list[bool]
    buttons: list[list[int]]
    button_press_count: int

    def __init__(self, machine_def):
        self.button_press_count = 0
        target_light_pattern_str, *button_wiring, _ = machine_def.split(" ")
        self.target_light_pattern = [y == "#" for y in target_light_pattern_str[1:-1]]
        self.current_light_pattern = [False] * len(self.target_light_pattern)

        self.buttons = []
        for button in button_wiring:
            self.buttons.append(list(map(int,button[1:-1].split(","))))

    def reset(self):
        self.current_light_pattern = [False] * len(self.target_light_pattern)
        self.button_press_count = 0

    def press_button(self, button_number):
        button_wiring = self.buttons[button_number]
        self.button_press_count += 1
        for light_to_flip in button_wiring:
            self.current_light_pattern[light_to_flip] = not self.current_light_pattern[light_to_flip]

    # takes in a binary string the length of the button list where 0 is a not pressed and 1 is pressed 
    def apply_button_pattern(self, button_pattern_string):
        for i in range(len(button_pattern_string)):
            if button_pattern_string[i] == "1":
                self.press_button(i)

def main():
    with(open("./input.txt", "r")) as fp:
        lines = map(str.strip, fp.readlines())

    total = 0

    for line in lines:
        m = Machine(line)
        button_count = len(m.buttons)
        fewest_presses = 9999999999
        for i in range(2**button_count):
            m.reset()
            button_pattern = "{0:b}".format(i).zfill(button_count)
            m.apply_button_pattern(button_pattern)

            if m.target_light_pattern == m.current_light_pattern and m.button_press_count < fewest_presses:
                fewest_presses = m.button_press_count
                
        total += fewest_presses

    print(f"total: {total}")


if __name__ == "__main__":
    main()