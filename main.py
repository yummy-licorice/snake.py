import random
import turtle
import time


WIDTH = 500
HEIGHT = 500
DELAY = 100  # Milliseconds
FOOD_SIZE = 20

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}


def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("left"), "Left")
    screen.onkey(lambda: set_snake_direction("right"), "Right")


def set_snake_direction(direction):
    global snake_direction
    if direction == "up":
        if snake_direction != "down":  # Prevents self collisions
            snake_direction = "up"
    if direction == "down":
        if snake_direction != "up":  # Prevents self collisions
            snake_direction = "down"
    if direction == "right":
        if snake_direction != "left":  # Prevents self collisions
            snake_direction = "right"
    if direction == "left":
        if snake_direction != "right":  # Prevents self collisions
            snake_direction = "left"


def game_loop():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Collisions
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
            or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        print(f"You Died!")
        text.write('Game Over!', font=("Arial", 30, "bold"), align='center')
        time.sleep(2)
        text.clear()
        reset()
    else:
        snake.append(new_head)

        if not food_collisions():
            snake.pop(0)  # Keep the length of the snake if no food collisions

        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        screen.title(f"Snake | Score: {score}")
        screen.update()
        turtle.ontimer(game_loop, DELAY)


def food_collisions():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False


def get_random_food_pos():
    x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y)


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance


def reset():
    global score, snake, snake_direction, food_pos
    score = 0
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    game_loop()


screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("#2e3440")
screen.tracer(0)

# Event Handlers
screen.listen()
bind_direction_keys()

stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()
stamper.color("#88c0d0")

# Food
food = turtle.Turtle()
food.shape("circle")
food.shapesize(FOOD_SIZE / 20)
food.penup()
food.color("#a3be8c")

text = turtle.Turtle()
text.penup()
text.hideturtle()
text.goto(250 / 20, 250 / 20)
text.color("#bf616a")

reset()

turtle.done()
