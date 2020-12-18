# Advent of Code: Day One

with open('input') as file_input:
    puzzle_input = file_input.read().strip().split()

print("*** ADVENT OF CODE: DAY ONE PUZZLE ***")

# Part One
# Iterate over each entry in the puzzle input, adding every other entry to it one by one in order to find which one has a sum of 2020.
# Then grab the product of the two numbers to solve the puzzle.

print("* Part One *")
partone_complete = False

for i in puzzle_input:
    each_puzzle_input = puzzle_input.copy()
    each_puzzle_input.remove(i)
    for e in each_puzzle_input:
        if int(e) + int(i) == 2020:
            print("The two values are {} and {}. Their multiplied result is {}.".format(e,i,int(e)*int(i)))
            partone_complete = True
        if partone_complete:
            break
    if partone_complete:
        break

# Part Two
# Do the same thing, but with three numbers instead!

print("* Part Two *")
parttwo_complete = False

for number1 in puzzle_input:
    input_with_one_removed = puzzle_input.copy()
    input_with_one_removed.remove(number1)
    for number2 in input_with_one_removed:
        input_with_two_removed = puzzle_input.copy()
        input_with_two_removed.remove(number1)
        input_with_two_removed.remove(number2)
        for number3 in input_with_two_removed:
            if int(number1) + int(number2) + int(number3) == 2020:
                print("The numbers are {}, {}, and {}. Their product is {}.".format(number1, number2, number3, int(number1) * int(number2) * int(number3)))
                parttwo_complete = True
            if parttwo_complete:
                break
        if parttwo_complete:
            break
    if parttwo_complete:
        break
