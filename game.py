import pygame

class Game:

    def __init__(self):
        self.player = Player()
        self.enemy = Enemy()

#génération de la fenetre
pygame.display.set_caption("The game")
screen = pygame.display.set_mode((1080,720))


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('peji.png')
        self.rect = self.image.get_rect()
        self.rect.x = 500

    def move_right(self):
        self.rect.x += self.velocity


    def move_left(self):
        self.rect.x -= self.velocity


    def move_up(self):
        self.rect.y += self.velocity


    def move_down(self):
        self.rect.y -= self.velocity


#Création d'énnemis
class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('tete.png')
        self.rect = self.image.get_rect()
        self.rect.x = 300
