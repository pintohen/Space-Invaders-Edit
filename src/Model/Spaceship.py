import os

import pygame


class Spaceship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("C:\\Users\\Henrique\\PycharmProjects\\game\\src\\Assets\\Spaceship.png")
        # flip the image upside down
        self.image = pygame.transform.flip(self.image, False, True)
        # scale the image
        self.scale = 0.1
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale), int(self.image.get_height() * self.scale)))
        self.width = self.image.get_width()
        self.height = self.image.get_height()


    def draw(self, screen):
        self.y += 2
        screen.blit(self.image, (self.x, self.y))
        return self

    @staticmethod
    def width():
        path = os.path.abspath("Assets\\Spaceship.png")
        img = pygame.image.load(path)
        img = pygame.transform.flip(img, False, True)
        scale = 0.1
        img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        return img.get_width()

    @staticmethod
    def height():
        path = os.path.abspath("Assets\\Spaceship.png")
        img = pygame.image.load(path)
        img = pygame.transform.flip(img, False, True)
        scale = 0.1
        img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        return img.get_height()