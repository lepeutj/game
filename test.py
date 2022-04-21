import pygame
from game import *

pygame.init()

#variables d'entrée
running = True

#boucle pour garder la fenêtre ouverte
while running:

#charger le jeu
    game = Game()

#appliquer l'image du joueur
    screen.blit(game.player.image,game.player.rect)
    screen.blit(game.enemy.image,game.enemy.rect)

#mettre à jour l'écran
    pygame.display.flip()


#maintenir la fenetre ouverte
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


#déplacement au clavier
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                print("droite")
                game.player.move_right()

            elif event.key == pygame.K_LEFT:
                print("gauche")
                game.player.move_left()

            elif event.key == pygame.K_UP:
                game.player.move_up()

            elif event.key == pygame.K_DOWN:
                game.player.move_down()
