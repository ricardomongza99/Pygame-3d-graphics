import pygame, sys, math, time


pygame.init()
WIDTH, HEIGHT = 800, 800

cx, cy = WIDTH // 2, HEIGHT // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

verts = (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
# front face; lines; back face
edges = (0, 1), (1, 2), (2, 3), (3, 0), \
        (0, 4), (1, 5), (2, 6), (3, 7), \
        (4, 5), (5, 6), (6, 7), (7, 4)

while True:
    dt = clock.tick()/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(BLACK)
    count = 0

    for edge in edges:

        points = []

        # iterates 2 times: uses (x, y, z) of edge 0 first then (x, y, z) of edge 1
        for x, y, z in (verts[edge[0]], verts[edge[1]]):

            z += 5

            f = 400 / z
            x *= f
            y *= f

            frequency = 4
            amplitude = cy // 2
            speed = 1

            nx = int(x + amplitude * math.cos(frequency * (cx) * (2 * math.pi) + time.time()))
            ny = int(y + amplitude * math.sin(frequency * (cy) * (2 * math.pi) + time.time()))

            points += [(cx+int(nx), cy+int(ny))]

        pygame.draw.line(screen, WHITE, (points[0]), (points[1]), 3)


    pygame.display.flip()

