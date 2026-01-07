import pygame
import sys

# ---------- Initialization ----------
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Game")

clock = pygame.time.Clock()

# ---------- Game settings ----------
SHIP_SPEED = 5
SCALE_FACTOR = 3  # how much bigger the sprite should be

# ---------- Load and prepare image ----------
ship = pygame.image.load("A-20g.png").convert_alpha()

# Scale the ship (VERY IMPORTANT)
ship = pygame.transform.scale_by(ship, SCALE_FACTOR)

# Get rectangle AFTER scaling
ship_rect = ship.get_rect()
ship_rect.centerx = SCREEN_WIDTH // 2
ship_rect.bottom = SCREEN_HEIGHT - 20  # keep it near bottom

# ---------- Game loop ----------
running = True
while running:
    clock.tick(60)  # 60 FPS

    # --- Events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Input ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship_rect.x -= SHIP_SPEED
    if keys[pygame.K_RIGHT]:
        ship_rect.x += SHIP_SPEED

    # Keep ship inside screen
    if ship_rect.left < 0:
        ship_rect.left = 0
    if ship_rect.right > SCREEN_WIDTH:
        ship_rect.right = SCREEN_WIDTH

    # --- Drawing ---
    screen.fill((0, 0, 0))      # clear screen
    screen.blit(ship, ship_rect)
    pygame.display.flip()

# ---------- Cleanup ----------
pygame.quit()
sys.exit(0)
