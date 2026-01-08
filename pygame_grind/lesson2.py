import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Lesson 2: Background Color")

PINK = (255, 128, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill(PINK)

        pygame.display.flip()

pygame.quit()
