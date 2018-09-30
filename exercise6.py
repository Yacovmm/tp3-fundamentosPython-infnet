import pygame
import random

pygame.init()
pygame.display.set_caption("--TP3 questão 5 YacovR.--")
size = width, heitgh = 800, 600

screen = pygame.display.set_mode(size)

green = (34, 139, 34)

clock = pygame.time.Clock()


class Quadradinho():
    def __init__(self):
        self.width = 50
        self.heitgh = 50
        self.x = random.randint(0, width - self.width)
        self.y = random.randint(0, heitgh - self.heitgh)
        self.color = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))
        self.area = pygame.Rect(self.x, self.y, self.width, self.heitgh)

    def draw(self, tela):
        pygame.draw.rect(tela, self.color, self.area)


q = Quadradinho()
q.draw(screen)

q = Quadradinho()


def main():
    done = True

    for i in range(0, 9):
        q = Quadradinho()
        q.draw(screen)

    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False


        clock.tick(60)
        pygame.display.update()

    pygame.quit()


main()
