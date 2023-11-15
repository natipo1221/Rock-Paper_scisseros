import pygame
import random


pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BACK = (255, 153, 153)
WIDTH = 1000
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock-Paper-Scissors")

# Font
FONT = pygame.font.SysFont('comicsans', 40)

# Counters
counter_user = 0
counter_computer = 0


def welcome_screen():
    input_text = ''
    while not input_text:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_text = True
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
        # Draw screen
        input_text_rect = pygame.Rect(WIDTH / 2 - 45, HEIGHT / 2 + 50, 90, 50)
        pygame.draw.rect(win, BLACK, input_text_rect, 2)
        win.fill(BACK)
        text = FONT.render("Welcome to the Rock-Paper-Scissors Game!", True, GREEN)
        text2 = FONT.render("Please enter R/P/S(rock/paper/scissors)", True, BLUE)

        win.blit(text, (WIDTH / 2 - text.get_width() / 2, 100))
        win.blit(text2, (WIDTH / 2 - text2.get_width() / 2, 200))
        pygame.display.update()


# Game loop
def game():
    global counter_user, counter_computer
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_r:
                    choice = 'rock'
                elif event.key == pygame.K_p:
                    choice = 'paper'
                elif event.key == pygame.K_s:
                    choice = 'scissors'
                else:
                    continue

                # Calculate result
                computer = random.choice(['rock', 'paper', 'scissors'])
                if computer == choice:
                    result = 'Tie'
                elif (choice == 'rock' and computer == 'scissors') or (
                        choice == 'paper' and computer == 'rock') or (choice == 'scissors' and computer == 'paper'):
                    result = 'Win'
                    counter_user += 1
                else:
                    result = 'Lose'
                    counter_computer += 1

                # Draw screen
                win.fill(WHITE)
                text1 = FONT.render(f'You chose {choice} and computer chose {computer}', True, BLACK)
                if result == 'Win':
                    text2 = FONT.render(f'{result}!', True, GREEN)
                elif result == 'Tie':
                    text2 = FONT.render(f'{result}!', True, YELLOW)
                elif result == 'Lose':
                    text2 = FONT.render(f'{result}!', True, RED)
                if counter_user > counter_computer:
                    text3 = FONT.render(f'Score: You {counter_user}-{counter_computer} Computer', True, GREEN)
                elif counter_computer > counter_user:
                    text3 = FONT.render(f'Score: You {counter_user}-{counter_computer} Computer', True, RED)
                elif counter_computer == counter_user:
                    text3 = FONT.render(f'Score: You {counter_user}-{counter_computer} Computer', True, YELLOW)
                win.blit(text1, (WIDTH / 2 - text1.get_width() / 2, 100))
                win.blit(text2, (WIDTH / 2 - text2.get_width() / 2, 200))
                win.blit(text3, (WIDTH / 2 - text3.get_width() / 2, 300))
                pygame.display.update()


welcome_screen()
game()
