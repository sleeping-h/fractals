from __future__ import division
import pygame
from pygame.locals import  * 
from math import sin, cos, atan, pi
pygame.init()

W, H = 700, 600
C = (W // 2, H // 2)
white = (255, 255, 255)
black = (0, 0, 0)
screen = pygame.display.set_mode((W, H), 0, 32)
screen.fill(white) 
phase = lambda (x1, y1), (x2, y2): atan((y1 - y2) / (x2 - x1 + 0.1)) + pi * (x2 - x1 < 0)
    
def rotate((x1, y1), (x0, y0), l):
    """rotation CCW,  angle l,  around x0, y0"""
    return ((x1 - x0) * cos(l) - (y1 - y0) * sin(l) + x0, 
            (x1 - x0) * sin(l) + (y1 - y0) * cos(l) + y0)
        
def line((x1, y1), (x2, y2), w):
    points = [(int(x1), int(H - y1)), (int(x2), int(H - y2))]
    pygame.draw.lines(screen, black, False, points, w // 2)
    
def tree(P1, P2, a, n):
    r = 0.33 # shortening of next branch,  nice at [0.31..0.48]
    (x1, y1), (x2, y2) = P1, P2
    if n:
        line(P1, P2, n)
        P3 = (x1 + (x2 - x1) * r, y1 + (y2 - y1) * r)
        tree(P2, rotate(P3, P2, a), a, n - 1)
        tree(P2, rotate(P3, P2, a + pi / 2), a, n - 1)
    else:                                                             
        pygame.draw.circle(screen, (0, 180, 20), (int(x1), int(H - y1)), 3, 1)   

mainloop = True
while mainloop:
    M = pygame.mouse.get_pos()
    tree((W // 2, 40), (W // 2, 220), phase(M, C) - 2.5, 11) # coords of stem
    pygame.display.update()
    screen.fill(white)
    for event in pygame.event.get():
        if event.type  ==  QUIT:
            mainloop = False
##    pygame.time.wait(20) # delay
pygame.quit()

