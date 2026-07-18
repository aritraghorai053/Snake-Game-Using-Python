#Libraries

import tkinter as tk       # =====>  Used to create GUI (Graphical User Interface).
import random              # =====>  Used to create GUI.

# Game Settings (Constants)

WIDTH = 600
HEIGHT = 600
SPEED = 200
SPACE_SIZE = 20
BODY_PARTS = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BG_COLOR = "black"

# Snake Class

class Snake:
    def __init__(self):   # Constructor
        self.coordinates = []  # Snake Coordinates
        self.squares = []           # Snake Body Squares

# Initial Snake Creation

        for i in range(BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(               # Drawing Snake
                x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                fill=SNAKE_COLOR, tag="snake"
            )
            self.squares.append(square)

# Food Class

class Food:
    def __init__(self):
        x = random.randint(0, (WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE,
            fill=FOOD_COLOR, tag="food"
        )

FOOD_COLORS = ["red", "yellow", "blue", "orange", "purple", "pink", "cyan"]

class Food:
    def __init__(self):

        x = random.randint(0, (WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE       # Random Position
        y = random.randint(0, (HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        color = random.choice(FOOD_COLORS)          #  Random Color

        canvas.create_oval(         # Draw Food
            x, y,
            x + SPACE_SIZE,
            y + SPACE_SIZE,
            fill=color,
            tag="food"
        )

# Snake Movement

def next_turn(snake, food):
    global score

    x, y = snake.coordinates[0]   # Get Snake Head

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE,
        fill=SNAKE_COLOR, tag="snake"
    )
    snake.squares.insert(0, square)

# Eating Food

    if x == food.coordinates[0] and y == food.coordinates[1]:

        score += 1
        label.config(text="Score: {}".format(score))

        canvas.delete("food")
        food = Food()

    else:
        del snake.coordinates[-1]       
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):     
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

#  Normal Movement

def change_direction(new_direction):
    global direction

    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction

#   Collision Detection

def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= WIDTH:
        return True
    elif y < 0 or y >= HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

# Game Over

def game_over():

    canvas.create_text(
        WIDTH / 2,
        HEIGHT / 2,
        text="GAME OVER",
        fill="red",
        font=("Arial", 30)
    )

# Restart Game

def restart_game():
    global snake, food, score, direction

    canvas.delete("all")

    score = 0
    direction = "down"

    label.config(text="Score: 0")

    snake = Snake()
    food = Food()

    next_turn(snake, food)


# Window
window = tk.Tk()
window.title("Snake Game 🐍")

score = 0
direction = "down"

label = tk.Label(window, text="Score: 0", font=("Arial", 14))
label.pack()

canvas = tk.Canvas(window, bg=BG_COLOR, height=HEIGHT, width=WIDTH)
canvas.pack()

restart_button = tk.Button(window, text="Restart", command=restart_game)
restart_button.pack()

# Keyboard Controls

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
