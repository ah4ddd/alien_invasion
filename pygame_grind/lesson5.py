import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Lesson 5: Loading Image")
clock = pygame.time.Clock()

SKY_BLUE = (135, 206, 235)

ship_image = pygame.image.load("B-17g.png")
ship_rect = ship_image.get_rect()

ship_rect.centerx = 400
ship_rect.bottom = 580

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill(SKY_BLUE)

        screen.blit(ship_image, ship_rect)

        pygame.display.flip()

pygame.quit()
