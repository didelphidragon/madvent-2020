# Advent of Code: Day Three
# dear god. ok i guess it's time for whatever this is
# navigate down the map at a 3/1 slope counting how many trees you encounter
# the map loops rightwards

# Part Two required checking other slopes and multiplying their tree totals,
# so i just repurposed Part One into taking custom slopes

print("** Advent of Code: Day Three (Parts One and Two) **")

with open('input') as file_input:
    puzzle_input = file_input.read().splitlines()

space_x = 1
space_y = 1
total_ouchie = 0
x_increment = int(input("Slope right?: "))
y_increment = int(input("Slope down?: "))

for i in puzzle_input: ################################ Somehow This Works
#    print("X={}\nY={}".format(space_x,space_y)) ###### And I Don't Care How
    if space_x > 31: ################################## As Long
        space_x = space_x - 31 ######################## As It
    try: ############################################## Works
        if puzzle_input[space_y - 1][space_x - 1] == "#": 
    #        print("ouch!")
            total_ouchie += 1
    except IndexError: # don't be naughty and indexerror at the end you fucking goober
        pass
    space_y += y_increment
    space_x += x_increment
print("Taking the slope 'right {} down {}', you encounter {} trees.".format(x_increment, y_increment, total_ouchie))