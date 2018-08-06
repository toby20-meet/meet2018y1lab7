import turtle
turtle.goto(0,0)

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
direction = None

print(direction)

def up():
    global direction
    direction = UP
    print("you pressed the up key.")
    print(direction)
    on_move()
    


def down():
    global direction
    direction = DOWN
    print("you pressed the down key.")
    print(direction)
    on_move()



def left():
    global direction
    direction = LEFT
    print('you pressed the left key')
    print(direction)
    on_move()



def right():
    global direction
    direction = RIGHT
    print("you pressed the right key")
    print(direction)
    on_move()


turtle.onkey(up,"Up")
turtle.onkey(down,'Down')
turtle.onkey(right,"Right")
turtle.onkey(left,'Left')
turtle.listen()

def on_move():
    (x,y) = turtle.pos()
    if direction == UP:
        turtle.goto(x,y+1)
    elif direction == DOWN:
        turtle.goto(x,y-1)
    elif direction == LEFT:
        turtle.goto(x-1,y)
    elif direction == RIGHT:
        turtle.goto(x+1,y)
