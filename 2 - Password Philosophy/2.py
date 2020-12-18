# Advent of Code: Day Two

# Part One: Determine how many valid passwords are present in the puzzle input following the formula:
# {low}-{high} {char}: {password}
# low: lowest amount of appearances of character for validity
# high: highest amount of appearances of character for validity
# char: the character to check
# password: the password to check

with open('input') as file_input:
    puzzle_input = file_input.read().split('\n')

print("** Part One **")

p1_total = 0
for i in puzzle_input:
    each_password = i.split(' ')
    policy_numbers = each_password[0].split('-')
    policy_character = each_password[1].replace(':','')
    policy_password = each_password[2]

    char_amount = policy_password.count(policy_character)
    if int(policy_numbers[0]) <= char_amount <= int(policy_numbers[1]):
        p1_total += 1
print("Total acceptable passwords: " + str(p1_total))

# Part Two: He Explained The Policy Wrong
# It's actually indexes instead of occurrence amounts!

print("** Part Two **")

p2_total = 0
for e in puzzle_input:
    each_password = e.split(' ')
    policy_numbers = each_password[0].split('-')
    policy_character = each_password[1].replace(':','')
    policy_password = each_password[2]

    char_amount = policy_password.count(policy_character)
    try:
        if (
            (policy_password[int(policy_numbers[0]) - 1] == policy_character and policy_password[int(policy_numbers[1]) - 1] != policy_character)
            or (policy_password[int(policy_numbers[0]) - 1] != policy_character and policy_password[int(policy_numbers[1]) - 1] == policy_character)
        ):
            p2_total += 1
    except IndexError:
        pass
print("Total acceptable passwords: " + str(p2_total))