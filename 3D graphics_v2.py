""""
Elaborado por Ricardo Montemayor
en construcción!
"""

import pygame, sys, math, time

# STATIC VARIABLES
WIDTH, HEIGHT = 600, 600
cx, cy = WIDTH // 2, HEIGHT // 2

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (221, 100, 208)
LBLUE = (43, 198, 255)

class Cuboid():
    z_offset = 6
    z_speed = 0.1
    x_speed = 0.1
    y_speed = 0.1
    t_rot = 0

    def __init__(self, pos, scale):
        self.pos = list(pos)
        self.scale = list(scale)
        self.verts = self.make_vertices(self.pos, self.scale)
        self.edges = (0, 1), (1, 2), (2, 3), (3, 0), \
                     (0, 4), (1, 5), (2, 6), (3, 7), \
                     (4, 5), (5, 6), (6, 7), (7, 4)
        self.origin = (pos[0] + scale[0]/2, pos[1] + scale[1]/2, pos[2] + scale[2]/2)

    def make_vertices(self, pos, scale):
        x, y, z = pos
        sx, sy, sz = scale

        points = []

        for i in range(8):
            if i == 0:
                points.append((x, y, z))
            elif i == 1:
                points.append((x + sx, y, z))
            elif i == 2:
                points.append((x + sx, y + sy, z))
            elif i == 3:
                points.append((x, y + sy, z))
            elif i == 4:
                points.append((x, y, z + sz))
            elif i == 5:
                points.append((x + sx, y, z + sz))
            elif i == 6:
                points.append((x + sx, y + sy, z + sz))
            elif i == 7:
                points.append((x, y + sy, z + sz))
        return points

    # the origin
    def update(self):
        self.origin = (self.verts[0][0] + self.scale[0]/2, self.verts[0][1] + self.scale[1]/2, self.verts[0][2] + self.scale[2]/2)

    def draw_points(self, screen):
        for x, y, z in self.verts:
            # move back
            z += self.z_offset
            # magnitude
            f = 400 / z
            x *= f
            y *= f
            pygame.draw.circle(screen, WHITE, (cx + int(x), cy + int(y)), 4)

    def draw_edges(self, screen, color):
        for edge in self.edges:
            points = []
            for x, y, z, in (self.verts[edge[0]], self.verts[edge[1]]):
                z += self.z_offset
                f = 400 / z
                x *= f
                y *= f
                # cx and cy centers
                points.append((cx + x, cy + y))
            pygame.draw.line(screen, color, points[0], points[1], 3)

    def draw_origin(self, screen, color):
        x, y, z = self.origin
        z+= self.z_offset
        f = 400 / z
        x*=f
        y*=f
        pygame.draw.circle(screen, color, (cx+int(x), cy+int(y)), 3)

    def move_fw_bw(self, dt):
        x, y, z = self.verts[0]
        # bounds
        if z >= 8 or z <= -4:
            self.z_speed = -(self.z_speed)
        z += self.z_speed
        self.verts = self.make_vertices((x, y, z), self.scale)

    def move_lf_rt(self, dt):
        x, y, z = self.verts[0]
        #  bounds
        if x >= 5 or x <= -5:
            self.x_speed = -(self.x_speed)
        x += self.x_speed
        self.verts = self.make_vertices((x, y, z), self.scale)

    def move_up_dn(self, dt):
        x, y, z = self.verts[0]
        #  bounds
        if y >= 5 or y <= -5:
            self.y_speed = -(self.y_speed)
        y += self.y_speed
        self.verts = self.make_vertices((x, y, z), self.scale)

    def move_bounce(self, dt):
        self.move_fw_bw(dt)
        self.move_lf_rt(dt)
        self.move_up_dn(dt)

    def rotate_right(self, dt):
        x, y, z = self.verts[0]

        self.verts = self.make_vertices((x, y, z), self.scale)


class Engine:
    # cubes created
    #cube = Cuboid_v2(pos=(-1, -1, -3), scale=(2, 2, 2), rot=(0, 0, 45))
    cube = Cuboid(pos=(-1, -1, -3), scale=(2, 2, 2))
    cube1 = Cuboid(pos=(3, 3, 0), scale=(2, 2, 1))
    cube2 = Cuboid(pos=(-4, -4, -3), scale=(3, 2, 2))

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("3D graphics v2")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.fps = 60.0
        self.done = False

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

    def update(self, dt):
        #self.cube.move_fw_bw(dt)
        self.cube1.move_fw_bw(dt)
        self.cube.move_bounce(dt)
        #self.cube.update()
        #self.cube1.move_bounce(dt)
        #self.cube1.update()
        self.cube2.move_bounce(dt)
        self.cube.rotate_right(dt)


    def draw(self):
        self.screen.fill(BLACK)

        self.cube.draw_edges(self.screen, PURPLE)
        #self.cube.draw_origin(self.screen, RED)

        #self.cube.draw_faces(self.screen)

        self.cube1.draw_edges(self.screen, GREEN)
        #self.cube1.draw_origin(self.screen, RED)

        self.cube2.draw_edges(self.screen, LBLUE)


    def main_loop(self):

        while not self.done:
            dt = self.clock.tick(self.fps) / 1000.0
            self.event_loop()
            self.update(dt)
            self.draw()
            pygame.display.flip()

            # key = pygame.key.get_pressed()
            # cube.move()


def main():
    app = Engine()
    app.main_loop()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

