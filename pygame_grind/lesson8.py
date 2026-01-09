from xmlrpc.client import TRANSPORT_ERROR
import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Lesson 8: Scaling")
clock = pygame.time.Clock()

SKY_BLUE = (135, 206, 235)

ship_image = pygame.image.load("B-17g.png").convert_alpha()

SCALE_FACTOR = 2
ship_image = pygame.transform.scale_by(ship_image, SCALE_FACTOR)

ship_rect = ship_image.get_rect()
ship_rect.centerx = 400
ship_rect.bottom = 580

ship_speed = 5

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        ship_rect.x -= ship_speed
    if keys[pygame.K_RIGHT]:
        ship_rect.x += ship_speed

    if ship_rect.left < 0:
        ship_rect.left = 0
    if ship_rect.right > 800:
        ship_rect.right = 800

    screen.fill(SKY_BLUE)
    screen.blit(ship_image, ship_rect)
    pygame.display.flip()

pygame.quit()
