import pygame
from random import shuffle
import time

# Initialization
pygame.init()

# Screen dimensions
screen_width = 250
screen_height = 250

# Game Screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sliding Puzzle')
pygame.display.update()
clock = pygame.time.Clock()

# Fonts
font1 = pygame.font.SysFont('calibri', 15)
font2 = pygame.font.SysFont('bold', 35)
font3 = pygame.font.SysFont('poppins', 30)


def display_text(text, font, text_color, x, y):
    '''This function is used to display text on screen.'''
    screen_text = font.render(text, True, text_color)
    screen.blit(screen_text, [x, y])


def plot_block(window, x, y, size, text, block_color='deep sky blue', font=font3, font_color='black'):
    '''This function is used to plot blocks on screen.'''
    pygame.draw.rect(window, block_color, [x, y, size, size])
    display_text(text, font, font_color, x + 20, y + 20)


def game():
    '''This function contains the main game loop and game variables.'''

    # Boolean variable
    game_start = False
    game_exit = False
    game_win = False

    # Coordinates of blocks
    block_coordinates = {'block1': [2, 2], 'block2': [64, 2], 'block3': [126, 2], 'block4': [188, 2],
                         'block5': [2, 64], 'block6': [64, 64], 'block7': [126, 64], 'block8': [188, 64],
                         'block9': [2, 126], 'block10': [64, 126], 'block11': [126, 126], 'block12': [188, 126],
                         'block13': [2, 188], 'block14': [64, 188], 'block15': [126, 188], 'black_block': [188, 188]}

    # Shuffling and plotting blocks
    if not game_start:
        game_start = True

        values = list(block_coordinates.values())
        shuffle(values)

        # Making a new coordinates dictionary with shuffled values
        block_coordinates = dict(zip(block_coordinates, values))

        screen.fill('black')

        plot_block(screen, block_coordinates['block1'][0], block_coordinates['block1'][1], 60, '1')
        plot_block(screen, block_coordinates['block2'][0], block_coordinates['block2'][1], 60, '2')
        plot_block(screen, block_coordinates['block3'][0], block_coordinates['block3'][1], 60, '3')
        plot_block(screen, block_coordinates['block4'][0], block_coordinates['block4'][1], 60, '4')
        plot_block(screen, block_coordinates['block5'][0], block_coordinates['block5'][1], 60, '5')
        plot_block(screen, block_coordinates['block6'][0], block_coordinates['block6'][1], 60, '6')
        plot_block(screen, block_coordinates['block7'][0], block_coordinates['block7'][1], 60, '7')
        plot_block(screen, block_coordinates['block8'][0], block_coordinates['block8'][1], 60, '8')
        plot_block(screen, block_coordinates['block9'][0], block_coordinates['block9'][1], 60, '9')
        plot_block(screen, block_coordinates['block10'][0], block_coordinates['block10'][1], 60, '10')
        plot_block(screen, block_coordinates['block11'][0], block_coordinates['block11'][1], 60, '11')
        plot_block(screen, block_coordinates['block12'][0], block_coordinates['block12'][1], 60, '12')
        plot_block(screen, block_coordinates['block13'][0], block_coordinates['block13'][1], 60, '13')
        plot_block(screen, block_coordinates['block14'][0], block_coordinates['block14'][1], 60, '14')
        plot_block(screen, block_coordinates['block15'][0], block_coordinates['block15'][1], 60, '15')

        pygame.draw.rect(screen, 'black', [block_coordinates['black_block'][0], block_coordinates['black_block'][1], 60, 60])

        black_block_coordinates = [[block_coordinates['black_block'][0], block_coordinates['black_block'][1]], [None, None]]


    # Gameloop
    while not game_exit:
        if game_win:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Capturing keys for controls
        keys = pygame.key.get_pressed()

        black_block_size = 60

        # Controls
        if keys[pygame.K_DOWN] and black_block_coordinates[0][1] > black_block_size + 2:
            black_block_coordinates[1][0], black_block_coordinates[1][1] = black_block_coordinates[0][0], black_block_coordinates[0][1]
            black_block_coordinates[0][1] -= black_block_size + 2

            # Pausing time for smooth controls
            time.sleep(0.2)

        if keys[pygame.K_UP] and black_block_coordinates[0][
            1] < screen_height - black_block_size - black_block_size + 2:
            black_block_coordinates[1][0], black_block_coordinates[1][1] = black_block_coordinates[0][0], black_block_coordinates[0][1]
            black_block_coordinates[0][1] += black_block_size + 2

            # Pausing time for smooth controls
            time.sleep(0.2)

        if keys[pygame.K_RIGHT] and black_block_coordinates[0][0] > black_block_size + 2:
            black_block_coordinates[1][0], black_block_coordinates[1][1] = black_block_coordinates[0][0], black_block_coordinates[0][1]
            black_block_coordinates[0][0] -= black_block_size + 2

            # Pausing time for smooth controls
            time.sleep(0.2)

        if keys[pygame.K_LEFT] and black_block_coordinates[0][
            0] < screen_width - black_block_size - black_block_size + 2:
            black_block_coordinates[1][0], black_block_coordinates[1][1] = black_block_coordinates[0][0], black_block_coordinates[0][1]
            black_block_coordinates[0][0] += black_block_size + 2

            # Pausing time for smooth controls
            time.sleep(0.2)


        # Plotting black block
        pygame.draw.rect(screen, 'black', [black_block_coordinates[0][0], black_block_coordinates[0][1], 60, 60])


        # Changing position of number blocks accordingly
        if abs(black_block_coordinates[0][0] - block_coordinates['block1'][0]) == 0 and abs(black_block_coordinates[0][1] - block_coordinates['block1'][1]) == 0:
            block_coordinates['block1'][0] = black_block_coordinates[1][0]
            block_coordinates['block1'][1] = black_block_coordinates[1][1]

            plot_block(screen, block_coordinates['block1'][0], block_coordinates['block1'][1], 60, '1')


        if abs(black_block_coordinates[0][0] - block_coordinates['block2'][0]) == 0 and abs(black_block_coordinates[0][1] - block_coordinates['block2'][1]) == 0:
            block_coordinates['block2'][0] = black_block_coordinates[1][0]
            block_coordinates['block2'][1] = black_block_coordinates[1][1]

            plot_block(screen, block_coordinates['block2'][0], block_coordinates['block2'][1], 60, '2')


        if abs(black_block_coordinates[0][0] - block_coordinates['block3'][0]) == 0 and abs(black_block_coordinates[0][1] - block_coordinates['block3'][1]) == 0:
            block_coordinates['block3'][0] = black_block_coordinates[1][0]
            block_coordinates['block3'][1] = black_block_coordinates[1][1]

            plot_block(screen, block_coordinates['block3'][0], block_coordinates['block3'][1], 60, '3')


        if abs(black_block_coordinates[0][0] - block_coordinates['block4'][0]) == 0 and abs(black_block_coordinates[0][1] - block_coordinates['block4'][1]) == 0:
            block_coordinates['block4'][0] = black_block_coordinates[1][0]
            block_coordinates['block4'][1] = black_block_coordinates[1][1]

            plot_block(screen, block_coordinates['block4'][0], block_coordinates['block4'][1], 60, '4')


        if abs(black_block_coordinates[0][0] - block_coordinates['block5'][0]) == 0 and abs(black_block_coordinates[0][1] - block_coordinates['block5'][1]) == 0:
            block_coordinates['block5'][0] = black_block_coordinates[1][0]
            block_coordinates['block5'][1] = black_block_coordinates[1][1]

            plot_block(screen, block_coordinates['block5'][0], block_coordinates['block5'][1], 60, '5')


        if abs(black_block_coordinates[0][0] - block_coordinates['block6'][0]) == 0 and abs(black_block_coordinates[0][1] - block_coordinates['block6'][1]) == 0:
            block_coordinates['block6'][0] = black_block_coordinates[1][0]
            block_coordinates['block6'][1] = black_block_coordinates[1][1]

            plot_block(screen, block_coordinates['block6'][0], block_coordinates['block6'][1], 60, '6')


        if abs(black_block_coordinates[0][0] - block_coordinates['block7'][0]) == 0 and abs(black_block_coordinates[0][1] - block_coordinates['block7'][1]) == 0:
            block_coordinates['block7'][0] = black_block_coordinates[1][0]
            block_coordinates['block7'][1] = black_block_coordinates[1][1]

            plot_block(screen, block_coordinates['block7'][0], block_coordinates['block7'][1], 60, '7')


        if abs(black_block_coordinates[0][0] - block_coordinates['block8'][0]) == 0 and abs(black_block_coordinates[0][1] - block_coordinates['block8'][1]) == 0:
            block_coordinates['block8'][0] = black_block_coordinates[1][0]
            block_coordinates['block8'][1] = black_block_coordinates[1][1]

            plot_block(screen, block_coordinates['block8'][0], block_coordinates['block8'][1], 60, '8')


        if abs(black_block_coordinates[0][0] - block_coordinates['block9'][0]) == 0 and abs(black_block_coordinates[0][1] - block_coordinates['block9'][1]) == 0:
            block_coordinates['block9'][0] = black_block_coordinates[1][0]
            block_coordinates['block9'][1] = black_block_coordinates[1][1]

            plot_block(screen, block_coordinates['block9'][0], block_coordinates['block9'][1], 60, '9')


        if abs(black_block_coordinates[0][0] - block_coordinates['block10'][0]) == 0 and abs(black_block_coordinates[0][1] - block_coordinates['block10'][1]) == 0:
            block_coordinates['block10'][0] = black_block_coordinates[1][0]
            block_coordinates['block10'][1] = black_block_coordinates[1][1]

            plot_block(screen, block_coordinates['block10'][0], block_coordinates['block10'][1], 60, '10')


        if abs(black_block_coordinates[0][0] - block_coordinates['block11'][0]) == 0 and abs(black_block_coordinates[0][1] - block_coordinates['block11'][1]) == 0:
            block_coordinates['block11'][0] = black_block_coordinates[1][0]
            block_coordinates['block11'][1] = black_block_coordinates[1][1]

            plot_block(screen, block_coordinates['block11'][0], block_coordinates['block11'][1], 60, '11')


        if abs(black_block_coordinates[0][0] - block_coordinates['block12'][0]) == 0 and abs(black_block_coordinates[0][1] - block_coordinates['block12'][1]) == 0:
            block_coordinates['block12'][0] = black_block_coordinates[1][0]
            block_coordinates['block12'][1] = black_block_coordinates[1][1]

            plot_block(screen, block_coordinates['block12'][0], block_coordinates['block12'][1], 60, '12')


        if abs(black_block_coordinates[0][0] - block_coordinates['block13'][0]) == 0 and abs(black_block_coordinates[0][1] - block_coordinates['block13'][1]) == 0:
            block_coordinates['block13'][0] = black_block_coordinates[1][0]
            block_coordinates['block13'][1] = black_block_coordinates[1][1]

            plot_block(screen, block_coordinates['block13'][0], block_coordinates['block13'][1], 60, '13')


        if abs(black_block_coordinates[0][0] - block_coordinates['block14'][0]) == 0 and abs(black_block_coordinates[0][1] - block_coordinates['block14'][1]) == 0:
            block_coordinates['block14'][0] = black_block_coordinates[1][0]
            block_coordinates['block14'][1] = black_block_coordinates[1][1]

            plot_block(screen, block_coordinates['block14'][0], block_coordinates['block14'][1], 60, '14')


        if abs(black_block_coordinates[0][0] - block_coordinates['block15'][0]) == 0 and abs(black_block_coordinates[0][1] - block_coordinates['block15'][1]) == 0:
            block_coordinates['block15'][0] = black_block_coordinates[1][0]
            block_coordinates['block15'][1] = black_block_coordinates[1][1]

            plot_block(screen, block_coordinates['block15'][0], block_coordinates['block15'][1], 60, '15')


        # Win check system
        if block_coordinates['block1'] == [2, 2] and \
                block_coordinates['block2'] == [64, 2] and \
                block_coordinates['block3'] == [126, 2] and \
                block_coordinates['block4'] == [188, 2] and \
                block_coordinates['block5'] == [2, 64] and \
                block_coordinates['block6'] == [64, 64] and \
                block_coordinates['block7'] == [126, 64] and \
                block_coordinates['block8'] == [188, 64] and \
                block_coordinates['block9'] == [2, 126] and \
                block_coordinates['block10'] == [64, 126] and \
                block_coordinates['block11'] == [126, 126] and \
                block_coordinates['block12'] == [188, 126] and \
                block_coordinates['block13'] == [2, 188] and \
                block_coordinates['block14'] == [64, 188] and \
                block_coordinates['block15'] == [126, 188] and \
                game_start:

            game_win = True

            # Displaying win screen
            screen.fill('deep sky blue')
            display_text('YOU WIN!', font2, 'black', 65, 95)
            display_text('Press ENTER to play again', font1, 'black', 50, 121)

        pygame.display.update()
        clock.tick(60)


def welcome_screen():
    '''This function displays the welcome screen.'''
    game_exit = False

    while not game_exit:
        # Displaying welcome screen
        screen.fill('deep sky blue')
        display_text('SLIDING', font2, 'black', 80, 60)
        display_text('PUZZLE', font2, 'black', 82, 82)
        display_text('Press ENTER to start', font1, 'black', 68, 108)
        display_text('[Use ARROW keys to play]', font1, 'black', 49, 155)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                game()

        pygame.display.update()
    pygame.quit()


# Function call
welcome_screen()
