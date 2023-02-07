import pygame


class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.image = pygame.image.load("C:\\Users\\Henrique\\PycharmProjects\\game\\src\\Assets\\Explosion.png")
        self.time = 0
        self.scale = 0.1
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale), int(self.image.get_height() * self.scale)))

    def draw(self, screen):
        self.time += 1
        screen.blit(self.image, (self.x, self.y))
        return self