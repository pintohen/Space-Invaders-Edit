import pygame


class Bar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 20
        # color = dark red
        self.color = (200, 0, 0)


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        # add a border to the rectangle
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height), 2)
        return self


    def move(self, x, screen):
        self.x += x
        self.draw(screen)
        pass
