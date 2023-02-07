import pygame.draw


class Bullet:

    def __init__(self, bar, screen):
        self.x = bar.x + bar.width / 2
        self.y = bar.y
        self.radius = 7
        # color = red
        self.color = (255, 0, 0)
        self.screen = screen
        self.speed = 10

    def draw(self):
        self.y -= self.speed
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

        return self