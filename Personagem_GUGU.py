import pygame,sys
from pygame.locals import *
import  Abertura
largura = 600
altura = 400
class Gugu_Personagem (pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.Direita1 = pygame.image.load('PersonagensGUGU/GUGUpatinete/direita.png')
        self.Direita = [self.Direita1 ] # lista de Imagem do GUGU

        self.Esquerda1 = pygame.image.load('PersonagensGUGU/GUGUpatinete/esquerda.png')
        self.Esquerda = [self.Esquerda1 ] # lista de Imagem do PATINETE

        self.GuGuPatinete1 = pygame.image.load('PersonagensGUGU/GUGUpatinete/Saindo.png')
        self.GuGuPatinete2 = pygame.image.load('PersonagensGUGU/GUGUpatinete/SaidaTotal.png')
        self.GuGuPatinete3 = pygame.image.load('PersonagensGUGU/GUGUpatinete/15.png')
        self.GuGuPatinete = [self.GuGuPatinete1 , self.GuGuPatinete2,self.GuGuPatinete3 ] # lista de Imagem do PATINETE

        self.patinete1 = pygame.image.load('PersonagensGUGU/GUGUpatinete/patinete.png')
        self.patinete = [self.patinete1]  # lista de Imagem do PATINETE

        self.brancoX = pygame.image.load('PersonagensGUGU/Branco.png')
        self.Branco = [self.brancoX]  # lista de Imagem do PATINETE

        self.depre0 = pygame.image.load('PersonagensGUGU/AndaDireita/14.png')
        self.depre1 = pygame.image.load('PersonagensGUGU/AndaDireita/8.png')

        self.depre = [ self.depre0 ,    self.depre1 ]  # lista de Imagem do PATINETE

        self.posImagem = 0 # variavel da posicao da lista de imagem do inimigo
        self.imagemGUGUAtual = self.Direita[self.posImagem] # cria image


        self.rect = self.imagemGUGUAtual.get_rect()
        self.listaDisparo = []
        self.velocidade = 0.5
        self.rect.top = posy
        self.rect.left = posx
        self.aumentaESCALA = 200

        self.configTempo = 0.0

    def setConfigTempo(self, configTempo ):
        self.configTempo = ( ( (( configTempo)) ))

    def getRect(self):
        return self.rect

    def setRectTop(self, top):
        self.rect.top = top

    def setRectLeft(self, esquerda):
        self.rect.left = esquerda

    def getRectLeft(self):
        return self.rect.left

    def getRectTop(self):
        return self.rect.top

    def andaDireita(self,valor):
        self.rect.left += valor

    def andaEsquerda(self,valor):
        self.rect.left -= valor

    def AumentaEscala(self):
        if self.aumentaESCALA < 500:
            velho = self.rect.center  # fazendo uma cópia do centro antigo do retângulo
            self.aumentaESCALA += 10
            self.imagemGUGUAtual = pygame.transform.smoothscale( self.imagemGUGUAtual , (self.aumentaESCALA , self.aumentaESCALA))
            self.rect = self.imagemGUGUAtual.get_rect()
            self.rect.center = velho  # defina o retângulo girado para o centro antigo


    def setEstadoFINAL(self,valor,posicao):
        if valor == 0:
            self.imagemGUGUAtual =self.Direita[posicao]
        if valor == 1:
            self.imagemGUGUAtual =self.Esquerda[posicao]
        if valor == 2:
            self.imagemGUGUAtual =self.GuGuPatinete[posicao]
        if valor == 3:
            self.imagemGUGUAtual =self.patinete[posicao]
        if valor == 4:
            self.imagemGUGUAtual =self.Branco[posicao]
        if valor == 5:
            self.imagemGUGUAtual =self.depre[posicao]

    def tipoImagem(self,valor):
        if valor == 0:
            self.imagemGUGUAtual = self.Direita[self.posImagem]
        if valor == 1:
            self.imagemGUGUAtual = self.Esquerda[self.posImagem]
        if valor == 2:
            self.imagemGUGUAtual =self.GuGuPatinete[self.posImagem]
        if valor == 3:
            self.imagemGUGUAtual =self.patinete[self.posImagem]
        if valor == 4:
            self.imagemGUGUAtual =self.Branco[self.posImagem]
        if valor == 5:
            self.imagemGUGUAtual =self.depre[self.posImagem]

    def EscolhaConjuntosImagens(self, valor):
        if valor == 0:
            return self.Direita
        if valor == 1:
            return self.Esquerda
        if valor == 2:
            return self.GuGuPatinete
        if valor == 3:
            return self.GuGuPatinete
        if valor == 4:
            return self.Branco
        if valor == 5:
            return self.depre

    def atualizaIMagens(self,tempo,valor,estado,escolha):   # troca a posicao do array lista do inimigo
      #  print('N1: %f' % (tempo) ,'------N2: %f' % (self.configTempo ) )

        if (self.configTempo) == ((tempo)):
                self.posImagem +=1;
                self.configTempo += valor
                if self.posImagem > len(self.EscolhaConjuntosImagens(escolha))-1:
                    self.posImagem = 0

        self.tipoImagem(estado)


    def colocar(self, superficie):
        superficie.blit(self.imagemGUGUAtual, self.rect)

