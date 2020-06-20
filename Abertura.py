import pygame,sys
from pygame.locals import *

largura = 732
altura = 532

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("OS Balulas")

class Abertura (pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.Imagem1 = pygame.image.load('Imagem/Abertura.png')
        self.imagemAbertura1 = self.Imagem1
        self.imagemAbertura2 = self.Imagem1

        self.listaImagem = [self.imagemAbertura1, self.imagemAbertura2 ] # lista de Imagem do inimigo
        self.posImagem = 0 # variavel da posicao da lista de imagem do inimigo

        self.imagemAlien = self.listaImagem[self.posImagem] # alien atual
        self.posx = posx
        self.posy = posy

        self.rect2 = self.Imagem1.get_rect()
        self.rect2.center = (largura // 2, altura // 2)

        self.configTempo = 6
        self.rot2 = 0
        self.rot_speed2 = 2
        self.tamanho = 1

    def getConfigTempo(self ):
        return self.configTempo

    def setConfigTempo(self, configTempo ):
        self.configTempo = configTempo


    def getTamanho(self):
        return self.tamanho

    def setTamanho(self, valor):
         self.tamanho=valor


    def rotacao(self,posicao,angulo,telaRODANDO):
        global rect2, rot2, rot_speed2,tamanho,tela
        self.rect2.center = posicao  # posicao do centro inicial
        old_center2 = self.rect2.center  # fazendo uma cópia do centro da figura
        self.rot2 = (self.rot2 + self.rot_speed2) % 360  # definindo o ângulo da rotação
        if angulo==0:
            Gira2 = pygame.transform.rotozoom(self.Imagem1, 0, self.tamanho)
        else:
            Gira2 = pygame.transform.rotozoom(self.Imagem1, self.rot2, self.tamanho)
            if self.tamanho > 0:
                self.tamanho-=0.01
            else:
                self.tamanho = -1
        self.rect2 = Gira2.get_rect()  # pega a figura atual girada
        self.rect2.center = old_center2  # recebe o valor do centro antigo

        telaRODANDO.blit(Gira2, self.rect2)  # mostra na tela

    def comportamento(self,tempo,tela):   # troca a posicao do array lista do inimigo
        if (self.configTempo == tempo and self.posImagem !=1 ):
            self.posImagem +=1;
            self.configTempo += 1
            if self.posImagem > len(self.listaImagem)-1:
                self.posImagem = 0

        if self.posImagem ==0:
            self.rotacao((self.posx , self.posy ),0,tela)
        else:

            self.rotacao((self.posx , self.posy ) ,1,tela)


