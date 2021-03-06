import pygame
from player import Player
# from settings import Clock, Window

pygame.init()

win_height = 500
win_width = 1920
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("First Game")

bg = pygame.image.load('images/bg.jpg')

p = Player(win)
# c = Clock()
# w = Window()

# variables
clock = pygame.time.Clock()
clockTime = 24  # Tied to player sprite count. Must be a multiple of 6 because there are 6 movement sprites

# Player animation and movement
def playerAnimation():
    if p.walk_count + 1 >= clockTime:
        p.walk_count = 0
    # If the player is moving left, the character sprite is flipped to face left
    if p.moving_left:
        win.blit(pygame.transform.flip(p.walk_anim[p.walk_count // 4], True, False), (p.player_x, p.player_y))
        p.walk_count += 1
        p.player_x -= p.player_speed
    elif p.moving_right:
        win.blit(p.walk_anim[p.walk_count // 4], (p.player_x, p.player_y))
        p.walk_count += 1
        p.player_x += p.player_speed
    # Makes it so when the player stops moving, the remain facing the correct direction
    else:
        if p.direction == "Left":
            win.blit(pygame.transform.flip(p.char, True, False), (p.player_x, p.player_y))
        else:
            win.blit(p.char, (p.player_x, p.player_y))


def redrawGameWindow():
    win.blit(bg, (0, 0))
    playerAnimation()
    pygame.display.update()


run = True
while run:
    clock.tick(clockTime)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Keydown events
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                p.moving_right = True
                p.moving_left = False
                p.direction = "Right"
            elif event.key == pygame.K_LEFT:
                p.moving_left = True
                p.moving_right = False
                p.direction = "Left"
            # Jump does not work
            elif event.key == pygame.K_UP:
                p.jump()

        # Keyup events
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                p.moving_right = False
            elif event.key == pygame.K_LEFT:
                p.moving_left = False
            elif event.key == pygame.K_UP:
                p.is_jump = False

    # w.drawGameWindow()
    redrawGameWindow()
    # p.update()

pygame.quit()
