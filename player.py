import pygame
'''
from settings import Settings

c = clock()
w = window()
'''


class Player:
    def __init__(self, screen):
        """Initialize the player and set its starting position."""
        self.screen = screen

        # Sprites
        self.walk_anim = [pygame.image.load('images/run-00.png'), pygame.image.load('images/run-01.png'),
                          pygame.image.load('images/run-02.png'), pygame.image.load('images/run-03.png'),
                          pygame.image.load('images/run-04.png'), pygame.image.load('images/run-05.png')]
        self.char = pygame.image.load('images/idle-00.png')

        # Set a variable for each movement.
        self.moving_right = False
        self.moving_left = False
        self.is_jump = False
        self.jump_count = 5
        self.walk_count = 0
        self.player_x = 50
        self.player_y = 440
        self.playerPos = [self.player_x, self.player_y]

       # # Load the player image and set player and screen to rect.
       # self.image = self.char
       # self.rect = self.image.get_rect()
       # self.screen_rect = screen.get_rect()

       # # Start the player at the bottom center of the screen.
       # self.rect.move(self.player_x, self.player_y)

        # Speed of the player
        self.player_speed = 5

        self.direction = ['right', 'left']

    # Not working
    """
    # Update the position of the player.
    def update(self):
        if self.rect.right <= self.screen_rect.right:
            if self.moving_right:
                self.rect.move(self.player_speed, 0)

        if self.rect.left > 0:
            if self.moving_left:
                self.rect.move(-self.player_speed, 0)
    """

    # Not working. Makes the player jump
    def jump(self):
        if self.is_jump:
            if self.jump_count >= -5:
                self.player_y -= (self.jump_count * abs(self.jump_count)) * 0.5
                self.jump_count -= 1
            else:
                self.jump_count = 10
                self.is_jump = False
