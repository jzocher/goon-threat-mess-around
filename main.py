import pygame

pygame.init()

win_height = 506
win_width = 900
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("First Game")

walk_right = [pygame.image.load('images/run-00.png'), pygame.image.load('images/run-01.png'),
              pygame.image.load('images/run-02.png'), pygame.image.load('images/run-03.png'),
              pygame.image.load('images/run-04.png'), pygame.image.load('images/run-05.png')]
walk_left = [pygame.image.load('images/run-00.png'), pygame.image.load('images/run-01.png'),
             pygame.image.load('images/run-02.png'), pygame.image.load('images/run-03.png'),
             pygame.image.load('images/run-04.png'), pygame.image.load('images/run-05.png')]
bg = pygame.image.load('images/bg.jpg')
char = pygame.image.load('images/idle-00.png')

# variables
clock = pygame.time.Clock()

player_x = 50
player_y = 406
player_width = 128
player_height = 128
player_vel = 5

is_jump = False
jump_count = 10

move_left = False
move_right = False
walk_count = 0


def redraw_game_window():
    global walk_count
    win.blit(bg, (0, 0))

    if walk_count + 1 >= 24:
        walk_count = 0

    if move_left:
        win.blit(walk_left[walk_count//4], (player_x, player_y))
        walk_count += 1
    elif move_right:
        win.blit(walk_right[walk_count//4], (player_x, player_y))
        walk_count += 1
    else:
        win.blit(char, (player_x, player_y))

    pygame.display.update()


run = True
while run:
    clock.tick(24)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > player_vel:
        player_x -= player_vel
        move_left = True
        move_right = False

    elif keys[pygame.K_RIGHT] and player_x < win_width - player_vel - player_width:
        player_x += player_vel
        move_right = True
        move_left = False
    else:
        move_left = False
        move_right = False
        walk_count = 0
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
            move_left = False
            move_right = False
            walk_count = 0
    else:
        if jump_count >= -10:
            player_y -= (jump_count * abs(jump_count)) * 0.5
            jump_count -= 1
        else:
            jump_count = 10
            is_jump = False
    redraw_game_window()

pygame.quit()
