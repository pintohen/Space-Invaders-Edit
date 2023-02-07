import pygame


class ScoreBoard:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont("Segoe UI", 30)
        self.text = self.font.render("Score: " + str(self.score), 1, (255, 255, 255))
        self.x = 10
        self.y = 10


    def draw(self, screen):
        self.text = self.font.render("Score: " + str(self.score), 1, (255, 255, 255))
        screen.blit(self.text, (self.x, self.y))
        return self

    def hitSpaceShip(self):
        self.score += 10
        return self