
# Name : Azizbek
# ID : U2110207


direction = ['Up', 'Right', 'Down', 'Left']
current_direction = 'Right'
y = 0
x = 0


def my_spaceship(command):
    global current_direction
    global direction
    global y
    global x


    if command == 'R':
        if direction.index(current_direction) == 3:
            current_direction = direction[0]
        else:
            current_direction = direction[direction.index(current_direction) + 1]
    elif command == 'L':
        current_direction = direction[direction.index(current_direction) - 1]
    elif command == 'A':
        if current_direction == 'Up':
            y += 1
        elif current_direction == 'Right':
            x += 1
        elif current_direction == 'Down':
            y -= 1
        else:
            x -= 1

    return f"y : {y}, x : {x}, Direction : {current_direction}"


# Input 0 to exit
while (True):
    command = str(input('Input values : '))
    if command == '0':
        break
    print(my_spaceship(command))

