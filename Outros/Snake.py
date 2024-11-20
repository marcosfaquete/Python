import pygame
from random import  randint

branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)

try:
    pygame.init()
except:
    print('O modulo pygame não foi inicializado com sucesso')

largura=640
altura=480
tamanho = 10

pos_x=randint(0,(largura-tamanho)/10)*10
pos_y=randint(0,(largura-tamanho)/10)*10
velocidade_x=0
velocidade_y=0
relogio = pygame.time.Clock()


fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Snake')

sair = True

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocidade_y=0
                velocidade_x=-tamanho
            if event.key == pygame.K_RIGHT:
                velocidade_y=0
                velocidade_x=tamanho
            if event.key == pygame.K_UP:
                velocidade_x=0
                velocidade_y=-tamanho
            if event.key == pygame.K_DOWN:
                velocidade_x=0
                velocidade_y=tamanho


    fundo.fill(branco)
    pygame.draw.rect(fundo, preto, [pos_x,pos_y,tamanho,tamanho])
    pos_x+=velocidade_x
    pos_y+=velocidade_y

    pygame.display.update()
    relogio.tick(20)
    if pos_x >= largura:
        pos_x=0
    if pos_x < 0:
        pos_x=largura-tamanho
    if pos_y >= altura:
        pos_y=0
    if pos_y < 0:
        pos_y=altura-tamanho

pygame.quit()
