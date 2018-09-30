import sys, pygame
import random

pygame.init()
pygame.display.set_caption("--TP3 questão 4 YacovR.--")

size = width, heitgh = 800, 600
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (220, 20, 60)
cor1 = (255, 122, 10)
cor2 = (122, 255, 10)
colors = [black, white, yellow, blue, red , cor1, cor2]

clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)

screen = pygame.display.set_mode(size)

# rect = pygame.draw.rect(screen, red, (100, 10, 100, 100), 50)
# circle = pygame.draw.circle(screen, blue, (400, 300), 50)

text_rect = font.render('Quadrado', False, yellow)
text_circle = font.render('Círculo', False, white)

cont = 0


def main(cont):
    done = True
    timer = 60
    build_object('rect', red, 100, 10, 100, 100, 0)
    build_object('circle', blue, 400, 300, 0, 0, 50)
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                done = False

        pygame.display.update()
        if cont == 180:
            c1 = random.choice(colors)
            c2 = random.choice(colors)

            text_write(text_rect, 110, 110)
            text_write(text_circle, 370, 370)

            build_object('rect', c1, 100, 10, 100, 100, 0)
            build_object('circle', c2, 400, 300, 0, 0, 50)

            cont = 0


        clock.tick(timer)
        cont = cont + 1
    pygame.quit()


def build_object(type, color, x, y, largura, altura, raio):
    if type == 'rect':
        pygame.draw.rect(screen, color, (x, y, largura, altura), raio)
    elif type == 'circle':
        pygame.draw.circle(screen, color, (x, y), raio)


def text_write(text, x1, y1):
    screen.blit(text, (x1, y1))

main(cont)