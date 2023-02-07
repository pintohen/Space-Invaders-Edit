import os
import random
import sys
import time

import pygame

from Model.Bar import Bar
from Model.Bullet import Bullet
from Model.Explosion import Explosion
from Model.ScoreBoard import ScoreBoard
from Model.Spaceship import Spaceship


def quit_or_not(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    else:
        pass


def updateBullets(bulletList):
    for bullet in bulletList:
        bullet.draw()
        if bullet.y < 0:
            bulletList.remove(bullet)


def updateDisplay(screen):
    FPS = 60  # frames per second setting
    pygame.display.update()  # update the screen
    pygame.time.Clock().tick(FPS)  # set the FPS
    screen.fill((0, 0, 0))  # fill the screen with black


def updateSpaceShips(spaceShipList, screen):
    for spaceShip in spaceShipList:
        spaceShip.draw(screen)
        if spaceShip.y > 600:
            spaceShipList.remove(spaceShip)


def bulletSpaceShipCollision(bulletList, spaceShipList, explosionList, myScoreBoard):
    for bullet in bulletList:
        for spaceShip in spaceShipList:
            if bullet.x > spaceShip.x and bullet.x < spaceShip.x + spaceShip.image.get_width() and bullet.y > spaceShip.y and bullet.y < spaceShip.y + spaceShip.image.get_height():
                bulletList.remove(bullet)
                spaceShipList.remove(spaceShip)
                explosionList.append(Explosion(spaceShip.x, spaceShip.y))
                myScoreBoard.hitSpaceShip()
                pathExplosionSound = os.path.abspath("Assets\\explosion.wav")
                pygame.mixer.music.load(pathExplosionSound)
                pygame.mixer.music.play(0)


def spaceShipHitBar(spaceShip, bar):
    if bar.x < spaceShip.x + spaceShip.image.get_width() and bar.x + bar.width > spaceShip.x and bar.y < spaceShip.y + spaceShip.image.get_height() and bar.y + bar.height > spaceShip.y:
        return True
    else:
        return False

def didYouLose(spaceShipList, bar):
    for spaceShip in spaceShipList:
        if spaceShip.y > 500 or spaceShipHitBar(spaceShip, bar):
            return True

    return False


def updateExplosions(explosionList, screen):
    for explosion in explosionList:
        explosion.draw(screen)
        if explosion.time > 20:
            explosionList.remove(explosion)


def didYouWin(myScoreBoard):
    return myScoreBoard.score >= 100


def __main__():
    # game setup
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space Invaders edited")

    # sound setup
    volume = 0.5
    pygame.mixer.music.set_volume(volume)

    # create the objects of the game (bar and scoreboard)
    myBar = Bar(350, 500)
    myScoreBoard = ScoreBoard()

    # list of objects of the game
    bulletList = []
    spaceShipList = []
    explosionList = []
    iterationsSinceLastBullet = 0
    iterationsSinceLastSpaceShip = 0

    # spaceship dimensions
    spaceShipWidth = Spaceship.width()
    spaceShipHeight = Spaceship.height()

    # booleans to check if the bar can move left or right
    canBarMoveLeft = True
    canBarMoveRight = True


    while True:
        myBar.draw(screen) # draw the bar

        for event in pygame.event.get():
            quit_or_not(event) # check if the user wants to quit

        movement = 0 # the movement of the bar (left or right)

        keys_pressed = pygame.key.get_pressed() # get the keys pressed by the user
        for key in keys_pressed:
            #print the key name
            if key:
                print(pygame.key.name(key))

        if keys_pressed[pygame.K_LEFT] and canBarMoveLeft:
            movement += -15 # move the bar to the left (negative movement)

        if keys_pressed[pygame.K_RIGHT] and canBarMoveRight:
            movement += 15 # move the bar to the right (positive movement)

        if keys_pressed[pygame.K_UP] and volume < 1:
            volume += 0.1
            pygame.mixer.music.set_volume(volume)

        if keys_pressed[pygame.K_DOWN] and volume > 0:
            volume -= 0.1
            pygame.mixer.music.set_volume(volume)

        if keys_pressed[pygame.K_SPACE] and iterationsSinceLastBullet >= 20:
            bulletList.append(Bullet(myBar, screen))
            iterationsSinceLastBullet = 0

        if iterationsSinceLastSpaceShip >= 100:
            spaceShipList.append(Spaceship(random.randint(0 + spaceShipWidth, 800 - spaceShipWidth), 0))
            iterationsSinceLastSpaceShip = 0

        iterationsSinceLastBullet += 1
        iterationsSinceLastSpaceShip += 1

        bulletSpaceShipCollision(bulletList, spaceShipList, explosionList, myScoreBoard)

        myBar.move(movement, screen) # move the bar if the user pressed a key
        canBarMoveRight = myBar.x + myBar.width < 800
        canBarMoveLeft = myBar.x > 0





        updateSpaceShips(spaceShipList, screen)
        updateBullets(bulletList)
        updateExplosions(explosionList, screen)
        myScoreBoard.draw(screen)



        if didYouLose(spaceShipList, myBar):
            # create a popup window and restart the game if the user wants to
            loser = "You lost!"
            loserFont = pygame.font.SysFont("Segoe UI", 50)
            loserText = loserFont.render(loser, True, (255, 255, 255))
            screen.blit(loserText, (300, 300))
            pygame.display.update()
            pathLosingSound = os.path.abspath("Assets\\losingSound.wav")
            pygame.mixer.music.load(pathLosingSound)
            pygame.mixer.music.play(0)
            time.sleep(2)
            __main__()

        if didYouWin(myScoreBoard):
            # create a popup window and restart the game if the user wants to
            winner = "You won!"
            winnerFont = pygame.font.SysFont("Segoe UI", 50)
            winnerText = winnerFont.render(winner, True, (255, 255, 255))
            screen.blit(winnerText, (300, 300))
            pygame.display.update()
            pathWinningSound = os.path.abspath("Assets\\winningSound.wav")
            pygame.mixer.music.load(pathWinningSound)
            pygame.mixer.music.play(0)
            time.sleep(2)
            __main__()



        updateDisplay(screen)  # update the display





if __name__ == '__main__':
    __main__()


