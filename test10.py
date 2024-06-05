import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
done = False
while not done:
for event in pygame.event.get():
if event.type == pygame.QUIT:
done = True
screen.fill((0, 0, 0))
pygame.draw.circle(screen, (255, 255, 255), [150, 95], 5, 3)
pygame.draw.circle(screen, (255, 255, 255), [135, 95], 5, 3)
pygame.draw.circle(screen, (255, 255, 255), [120, 95], 5, 3)
pygame.draw.circle(screen, (255, 255, 255), [105, 100], 5, 3)
pygame.draw.circle(screen, (255, 255, 255), [90, 110], 5, 3)
pygame.draw.circle(screen, (255, 255, 255), [85, 130], 5, 3)
pygame.draw.circle(screen, (255, 255, 255), [85, 150], 5, 3)
pygame.draw.circle(screen, (255, 255, 255), [90, 170], 5, 3)
pygame.draw.circle(screen, (255, 255, 255), [110, 185], 5, 3)
pygame.draw.circle(screen, (255, 255, 255), [140, 195], 5, 3)
pygame.draw.circle(screen, (255, 255, 255), [170, 195], 5, 3)
pygame.draw.circle(screen, (255, 255, 255), [200, 190], 5, 3)
pygame.draw.circle(screen, (255, 255, 255), [230, 180], 5, 3)
pygame.draw.circle(screen, (255, 255, 255), [250, 160], 5, 3)
pygame.draw.ellipse(screen, (255, 0, 0), [100, 100, 100, 70], 10)
pygame.display.flip()
clock.tick(30)
pygame.quit()

b)

import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
while not done:
for event in pygame.event.get():
if event.type == pygame.QUIT:
done = True
pygame.draw.circle(screen, (255,255,255), [100, 80], 10, 0)
pygame.draw.circle(screen, (0,0,0), [100, 80], 10, 0)
pygame.draw.circle(screen, (255,255,255), [150, 95], 10, 0)
pygame.draw.circle(screen, (0,0,0), [150, 95], 10, 0)
pygame.draw.circle(screen, (255,255,255), [200, 130], 10, 0)
pygame.draw.circle(screen, (0,0,0), [200, 130], 10, 0)
pygame.draw.circle(screen, (255,255,255), [250, 150], 10, 0)
pygame.display.update()
pygame.quit()