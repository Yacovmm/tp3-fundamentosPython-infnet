import pygame
import random

pygame.init()
pygame.display.set_caption("--TP3 questão 5 YacovR.--")
size = width, heitgh = 800, 600

screen = pygame.display.set_mode(size)

green = (34, 139, 34)

x = random.randint(0, width - 250)
y = random.randint(0, heitgh - 250)

area = pygame.Rect(x, y, 250, 250)


def main():
    done = True

    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                done = False

        pygame.draw.rect(screen, green, area)
        pygame.display.update()

    pygame.quit()


main()
