import pygame, math, time

pygame.init()
WIDTH, HEIGHT = 800, 800

cx, cy = WIDTH // 2, HEIGHT // 2
unit = cx // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
WHITE = (255, 255, 255)

t = 0


while True:
    dt = clock.tick() / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(BLACK)

    pygame.draw.circle(screen, (50, 50, 50), (cx, cy), cx//2)

    x = int(cx + math.sin(t * math.pi) * unit)
    y = int(cy - math.cos(t * math.pi) * unit)


    pygame.draw.circle(screen, WHITE, (x, y), 6)

    pygame.display.flip()

    clock.tick(60)

    if t >= 2:
        t=0
    t += 0.01