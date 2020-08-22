import sys
import math
import pygame as pg


class Block(pg.sprite.Sprite):
    def __init__(self, pos, speed):
        self.image = pg.Surface((50, 50)).convert()
        self.image.fill(pg.Color("red"))
        self.rect = self.image.get_rect(center=pos)
        self.exact_position = list(self.rect.center)
        self.speed = speed  # Pixels per second
        self.target = None
        self.vec = None
        self.distance = None

    def update(self, dt):
        if self.target:
            travelled = math.hypot(self.vec[0] * dt, self.vec[1] * dt)
            self.distance -= travelled
            if self.distance <= 0:
                self.rect.center = self.exact_position = self.target
                self.target = None
            else:
                self.exact_position[0] += self.vec[0] * dt
                self.exact_position[1] += self.vec[1] * dt
                self.rect.center = self.exact_position

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def get_new_instruction(self, target):
        x = target[0] - self.exact_position[0]
        y = target[1] - self.exact_position[1]
        self.distance = math.hypot(x, y)
        try:
            self.vec = self.speed * x / self.distance, self.speed * y / self.distance
            self.target = list(target)
        except ZeroDivisionError:
            pass


class Control(object):
    def __init__(self):
        pg.init()
        pg.display.set_caption("Move To Target")
        self.screen = pg.display.set_mode((500, 500))
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.done = False
        self.player = Block(self.screen_rect.center, 500)

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.player.get_new_instruction(event.pos)

    def update(self, dt):
        self.player.update(dt)

    def draw(self):
        self.screen.fill((30, 40, 50))
        self.player.draw(self.screen)

    def main_loop(self):
        while not self.done:
            dt = self.clock.tick(self.fps) / 1000.0
            self.event_loop()
            self.update(dt)
            self.draw()
            pg.display.update()


def main():
    app = Control()
    app.main_loop()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()