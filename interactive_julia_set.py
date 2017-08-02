from __future__ import division
import pygame
from pygame.locals import *

def iterate(z, c, k=0):
    step = 536.842 / (k + 13.42)
    if k > 255:
        return 255 
    elif abs(z) > 2:
        return int(k * k / 255)
    return iterate(z ** 2 + c, c, k + step)

scale = 80
mx0, jx0, y0 = -2.5, -1.9, -1.5

W, H = 600, -int(2 * y0 * scale)
jW, jH = 300, H
jX, jY = 0, 0
mW, mH = W - jW, H
mX, mY = jX + jW, 0

pygame.init()
screen = pygame.display.set_mode((W, H), 0, 32)
screen.fill((0, 0, 0))
pygame.draw.rect(screen, (64, 64, 64), (mX, 0, 6, H), 0)
pygame.display.update()


for x in range(7, mW): # Mandelbrot
    for y in range(mH):
        c = x / scale + mx0 + 1j * (y / scale + y0)
        k = iterate(0, c)
        screen.set_at((x + mX, H - y + mY), (k, k, k))
    pygame.display.update()

mainloop = True
while mainloop:
    for event in pygame.event.get():
        if event.type == QUIT:
            mainloop = False
    x, y = pygame.mouse.get_pos()
    cx = (x - mX) / scale + mx0
    cy = (H - y - mY) / scale + y0
    c = cx + cy * 1j
    for x in range(jW): # Julia
        for y in range(jH):
            k = iterate(x / scale + jx0 + (y / scale + y0) * 1j, c)
            screen.set_at((x + jX, H - y + jY), (k, k, k))
    t = pygame.font.SysFont("monospace", 14)
    text = "C = %s + %si" % (round(cx, 3), round(cy, 3))
    t1 = t.render(text, 0, (128, 128, 128))
    screen.blit(t1, (0, 0)) 
    pygame.display.update()
pygame.quit()
