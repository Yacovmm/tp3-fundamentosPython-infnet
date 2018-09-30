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
        self.red = (220, 20, 60)
        self.area = pygame.Rect(self.x, self.y, self.width, self.heitgh)

    def draw(self, tela):
        pygame.draw.rect(tela, self.red, self.area)







def main():
    done = True

    q = Quadradinho()
    q_pos = q.x , q.y
    q.draw(screen)

    while done:
        for event in pygame.event.get():

            if event.type ==pygame.MOUSEBUTTONDOWN:

                x = pygame.mouse.get_pos()
                print(x)
                print(q_pos)
                if q.area.collidepoint(x):
                    screen.fill((0,0,0))

            if event.type == pygame.QUIT:
                done = False


        clock.tick(60)
        pygame.display.update()

    pygame.quit()


main()
