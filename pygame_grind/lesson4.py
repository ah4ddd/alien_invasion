import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Lesson 4: Drawing Shapes")
clock = pygame.time.Clock()

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill(BLACK)

        pygame.draw.rect(screen, RED, (100, 100, 200, 150))

        pygame.draw.circle(screen, GREEN, (400, 300), 60)

        pygame.draw.line(screen, BLUE, (0, 0), (800, 600), 5)

        pygame.display.flip()

pygame.quit()
