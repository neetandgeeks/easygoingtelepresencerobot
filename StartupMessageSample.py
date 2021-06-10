# -*- coding: utf-8 -*-

import sys
import pygame
import time

# Fonts
PixelMplus10Regular = "PixelMplus10-Regular.ttf"
PixelMplus10Bold = "PixelMplus10-Bold.ttf"

pygame.init()
resolution = 640,480
#screen = pygame.display.set_mode(resolution ,pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.NOFRAME)
screen = pygame.display.set_mode(resolution)
#pygame.display.quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.display.quit()
                sys.exit()

    black = 0,0,0
    white = 255,255,255
    wasurenagusairo = 119,184,218 #sRGB
    usuiro = 168,105,190 #sRGB
    giallo_di_piombo = 241,223,100 #sRGB
    coordinate = 75,90
    wc0, hc0 = coordinate
    screen.fill(black)
    pygame.display.update()
    pygame.font.init()
    font00 = pygame.font.Font(PixelMplus10Regular,14)
    font = pygame.font.Font(PixelMplus10Regular,60)

#    message00 = "YUKI.N> 見えてる？"
#    message01 = "(´・ω・`)"
    message01 = "Next-age"
    message01_list = list(message01)
    message02 = "Enhanced"
    message02_list = list(message02)
    message03 = "Equipment"
    message03_list = list(message03)
    message04 = "Technology"
    message04_list = list(message04)
    message05 = "NEET&"
    message05_list = list(message05)
    message06 = "GEEKS"
    message06_list = list(message06)
    message07 = "PRESENTS"
    message07_list = list(message07)

#    for i in message00_list:
#        coordinate00 = 10,10
#        wc,hc = coordinate
#        w,h = font.size(i)
#        dialogue = font.render(i, True, white)
#        screen.blit(dialogue, coordinate)
#        pygame.display.update()
#        time.sleep(0.15)
#        coordinate = w + wc, hc

    for i in message01_list:
        wc,hc = coordinate
        w,h = font.size(i)
        dialogue = font.render(i, True, white)
        screen.blit(dialogue, coordinate)
        pygame.display.update()
        time.sleep(0.1)
        coordinate = w + wc, hc

    wc, hc = coordinate
    coordinate = wc0, hc + h
    time.sleep(0.15)

    for i in message02_list:
        wc,hc = coordinate
        w,h = font.size(i)
        dialogue = font.render(i, True, white)
        screen.blit(dialogue, coordinate)
        pygame.display.update()
        time.sleep(0.1)
        coordinate = w + wc, hc

    wc, hc = coordinate
    coordinate = wc0, hc + h
    time.sleep(0.15)

    for i in message03_list:
        wc,hc = coordinate
        w,h = font.size(i)
        dialogue = font.render(i, True, white)
        screen.blit(dialogue, coordinate)
        pygame.display.update()
        time.sleep(0.1)
        coordinate = w + wc, hc

    wc, hc = coordinate
    coordinate = wc0, hc + h
    time.sleep(0.15)

    for i in message04_list:
        wc,hc = coordinate
        w,h = font.size(i)
        dialogue = font.render(i, True, white)
        screen.blit(dialogue, coordinate)
        pygame.display.update()
        time.sleep(0.1)
        coordinate = w + wc, hc

    wc, hc = coordinate
    coordinate = wc0, hc0
    time.sleep(0.15)

    for i in message05_list:
        wc,hc = coordinate
        w,h = font.size(i)
        dialogue = font.render(i, True, wasurenagusairo)
        screen.blit(dialogue, coordinate)
        pygame.display.update()
        time.sleep(0.1)
        coordinate = wc, h + hc

    wc, hc = coordinate
    coordinate = wc0+450, hc0
    time.sleep(0.15)

    for i in message06_list:
        wc,hc = coordinate
        w,h = font.size(i)
        dialogue = font.render(i, True, usuiro)
        screen.blit(dialogue, coordinate)
        pygame.display.update()
        time.sleep(0.1)
        coordinate = wc, h + hc

    wc, hc = coordinate
    coordinate = wc0+240, hc - h
    time.sleep(0.15)

    for i in message07_list:
        wc,hc = coordinate
        w,h = font.size(i)
        dialogue = font.render(i, True, giallo_di_piombo)
        screen.blit(dialogue, coordinate)
        pygame.display.update()
        time.sleep(0.1)
        coordinate = w + wc, hc

    time.sleep(1)
