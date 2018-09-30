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
        self.black = (0, 0, 0)
        self.width = 50
        self.heitgh = 50
        self.x = random.randint(0, width - self.width)
        self.y = random.randint(0, heitgh - self.heitgh)
        self.color = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))
        self.area = pygame.Rect(self.x, self.y, self.width, self.heitgh)

    def draw(self, tela):
        pygame.draw.rect(tela, self.color, self.area)

    def remove(self, screen):
        pygame.draw.rect(screen, self.black, self.area)





def main():
    done = True

    lista = []
    for i in range(0, 10):
        q = Quadradinho()
        q.draw(screen)
        lista.append(q)

    while done:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for q in lista:
                    if q.area.collidepoint(pos):
                        q.remove(screen)

        clock.tick(60)
        pygame.display.update()

    pygame.quit()


main()
