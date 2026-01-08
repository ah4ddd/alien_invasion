import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Lesson 3: Frame Rate")

clock = pygame.time.Clock()

YELLOW = (200, 155, 60)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill(YELLOW)
        pygame.display.flip()

pygame.quit()
