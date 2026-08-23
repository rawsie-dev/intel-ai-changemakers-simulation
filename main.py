import pygame
from core.game import Game

pygame.init()
screen = pygame.display.set_mode((1200, 675))
clock = pygame.time.Clock()
game = Game()
running = True

while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.update(dt)
    game.draw(screen)
    pygame.display.flip()

pygame.quit()