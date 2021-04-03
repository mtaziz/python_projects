import pygame
import random
import os

# Initialization
pygame.init()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# Screen width and height.
s_width = 500
s_height = 500

# Game Screen
screen = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Snake Game')
pygame.display.update()
clock = pygame.time.Clock()

# Fonts
font1 = pygame.font.SysFont('calibri', 15)
font2 = pygame.font.SysFont('bold', 50)
font3 = pygame.font.SysFont('poppins', 60)

def display_text(text, font, color, x, y):
    '''This function is used to display text on screen.'''
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x, y])

def plot_snake(window, color, coordinates, size):
    '''This function is used to plot snake on screen.'''
    for x, y in coordinates:
        pygame.draw.rect(window, color, [x, y, size, size])

def welcome_screen():
    '''This function displays the welcome screen.'''
    game_exit = False
    while not game_exit:
        screen.fill(black)
        display_text('SNAKES', font3, blue, 155, 220)
        display_text('Press ENTER to play.', font1, white, 185, 260)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game()
        pygame.display.update()
        clock.tick(40)

def game():
    '''This function contains the main game loop and game variables.'''
    # Boolean variables
    game_exit = False
    game_over = False

    # Coordinates of snake
    snake_x = 245
    snake_y = 245

    # Variable for moving snake.
    velocity_x = 0
    velocity_y = 0

    # Speed
    change_velocity = 5

    # Random coordinates of food.
    food_x = random.randint(20, s_width - 20)
    food_y = random.randint(20, s_height - 20)

    # Variable to increase and control the size of the snake.
    snake_list = []
    snake_length = 1

    # Score
    score = 0

    # Checking if the file exits and creating it if not present.
    if not os.path.exists('highscore.txt'):
        with open('highscore.txt', 'w') as f:
            f.write('0')

    # Storing the file content in a variable.
    with open('highscore.txt', 'r') as f:
        high_score = f.read()

    # Gameloop
    while not game_exit:
        if game_over:
            # Writing highscore in the file.
            with open('highscore.txt', 'w') as f:
                f.write(str(high_score))
            screen.fill(black)
            display_text('Game Over!', font2, white, 150, 220)
            display_text('Press ENTER to continue...', font1, white, 175, 255)
            display_text('Press r to reset the high score.', font1, red, 5, 5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    with open('highscore.txt', 'w') as f:
                        f.write(str(high_score))
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game()
                    if event.key == pygame.K_r:
                        with open('highscore.txt', 'w') as f:
                            f.write('0')

                        # Function call
                        game()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True

                # Controls
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        velocity_y = -change_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = change_velocity
                        velocity_x = 0
                    if event.key == pygame.K_RIGHT:
                        velocity_x = change_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -change_velocity
                        velocity_y = 0

            # Changing snake's position.
            snake_x += velocity_x
            snake_y += velocity_y

            # Eat mechanism
            if abs(snake_x - food_x) < 8 and abs(snake_y - food_y) < 8:
                snake_length += 2
                score += 10
                food_x = random.randint(20, s_width - 20)
                food_y = random.randint(20, s_height - 20)

            screen.fill(black)
            display_text('SCORE: ' + str(score), font1, green, 155, 5)
            display_text('HIGH SCORE: ' + high_score, font1, green, 255, 5)
            head = [snake_x, snake_y]
            snake_list.append(head)

            # Controlling snake's length to stop it from keep growing.
            if len(snake_list) > snake_length:
                del snake_list[0]

            # These two conditions below will check for death.
            if snake_x == 0 or snake_x == s_width or snake_y == 0 or snake_y == s_height:
                if score > int(high_score):
                    high_score = score
                game_over = True

            if head in snake_list[:-1]:
                if score > int(high_score):
                    high_score = score
                game_over = True

            # Plotting snake
            plot_snake(screen, white, snake_list, 10)
            # Plotting food
            pygame.draw.rect(screen, blue, [food_x, food_y, 10, 10])

        pygame.display.update()
        clock.tick(60)

    quit()
    pygame.quit()

# Function call
welcome_screen()
