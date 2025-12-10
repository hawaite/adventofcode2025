import pulp

def main():
    with(open("./input.txt", "r")) as fp:
        lines = map(str.strip,fp.readlines())

    total = 0

    for line in lines:
        _, *button_defs, joltage_targets_str = line.split(" ")
        joltage_targets = list(map(int,joltage_targets_str[1:-1].split(",")))
        buttons = []
        for button in button_defs:
            buttons.append(list(map(int, button[1:-1].split(","))))

        # Problem is integer linear program so we will use pulp as the ILP solver
        
        A = []
        # now we need to add 1 row PER COUNTER with a 1 if that button index affects this counter, and 0 if it doesnt
        for counter_number in range(len(joltage_targets)):
            row = [0] * len(buttons)
            # iterate all the buttons, and if a button affects this counter, make that index a 1
            for button_number in range(len(buttons)):
                if counter_number in buttons[button_number]:
                    row[button_number] = 1

            A.append(row)

        button_count = len(buttons)
        counter_count = len(joltage_targets)

        # Define problem
        prob = pulp.LpProblem("ButtonPresses", pulp.LpMinimize)

        # set up a variable representing how many times each button has been pressed so pulp can mess with it
        variables = [pulp.LpVariable(f"x_{j}", lowBound=0, cat="Integer") for j in range(button_count)]

        # we want pulp to test if this is an optimal solution by summing up the values of all the variables
        # which just means summing the button press counts
        prob += pulp.lpSum(variables)

        # add constraint for each counter that the sum of 
        # (number of times button was pressed (variable) * value this button incriments this counter) must 
        # equal the joltage target for that counter
        for counter_ix in range(counter_count):
            terms = []
            for button_ix in range(button_count):
                # here we need to build (amount button increases counter by (which is 0 or 1)) * number of presses of that button (from the pulp managed variable)
                amount_button_increases_counter = A[counter_ix][button_ix]
                amount_of_presses_of_this_button = variables[button_ix]
                terms.append(amount_button_increases_counter * amount_of_presses_of_this_button)
            expression = pulp.lpSum(terms)

            print(terms)

            # then we add a constraint that this expression must match the joltage target
            prob += expression == joltage_targets[counter_ix]

        result = prob.solve()

        if pulp.LpStatus[result] == "Optimal":
            presses = [int(pulp.value(var)) for var in variables]
            total += sum(presses)
        print("--------------------")

    print(f"total: {total}")
if __name__ == "__main__":
    main()