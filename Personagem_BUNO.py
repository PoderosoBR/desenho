import pygame,sys
from pygame.locals import *
import  Abertura
largura = 600
altura = 400
class Buno_Personagem (pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagem1 = pygame.image.load('PersonagensBuno/AndaDireita/8.png')
        self.imagem2 = pygame.image.load('PersonagensBuno/AndaDireita/9.png')
        self.imagem3 = pygame.image.load('PersonagensBuno/AndaDireita/11.png')
        self.imagensDireita = [self.imagem1, self.imagem2, self.imagem3 ] # lista de Imagem do inimigo

        self.supresa0 = pygame.image.load('PersonagensBuno/Supresa/0.png')
        self.supresaInicial = [self.supresa0]  # lista de Imagem do inimigo

        self.supresa1 = pygame.image.load('PersonagensBuno/Supresa/1.png')
        self.supresa2 = pygame.image.load('PersonagensBuno/Supresa/2.png')
        self.supresa3 = pygame.image.load('PersonagensBuno/Supresa/3.png')

        self.supresaFinal = [self.supresa1  ,  self.supresa2, self.supresa3 ]  # lista de Imagem do inimigo

        self.patinete1 = pygame.image.load('PersonagensBuno/BunoPatinete/sobe.png')
        self.patinete2 = pygame.image.load('PersonagensBuno/BunoPatinete/encima.png')
        self.patinete3 = pygame.image.load('PersonagensBuno/BunoPatinete/bate.png')
        self.patinete4 = pygame.image.load('PersonagensBuno/BunoPatinete/SaiuVOANDO.png')

        self.patinete = [self.patinete1, self.patinete2, self.patinete3,  self.patinete4  ]  # lista de Imagem do inimigo

        self.andandoPatinete1 = pygame.image.load('PersonagensBuno/BunoPatinete/encima.png')
        self.andandoPatinete = [self.andandoPatinete1]  # lista de Imagem do inimigo

        self.cama0 = pygame.image.load('PersonagensBuno/CAMA/cai.png')
        self.cama1 = pygame.image.load('PersonagensBuno/CAMA/Deitado.png')
        self.cama2 = pygame.image.load('PersonagensBuno/Branco.png')

        self.cama = [ self.cama0 , self.cama1 , self.cama2]  # lista de Imagem do inimigo


        self.posImagem = 0 # variavel da posicao da lista de imagem do inimigo
        self.imagemBunoAtual = self.imagensDireita[self.posImagem] # cria image


        self.rect = self.imagemBunoAtual.get_rect()
        self.listaDisparo = []
        self.velocidade = 0.5
        self.rect.top = posy
        self.rect.left = posx
        self.colisao = False

        self.configTempo = 0.0

    def setConfigTempo(self, configTempo ):
        self.configTempo = ( ( (( configTempo)) ))

    def getColisao(self):
        return self.colisao

    def setColisao(self, valor):
         self.colisao = valor

    def verificaColisao(self,rect2,valor,posicao):                 # VERIFICA A COLISAO DO LUCAS COM OS OUTROS
        if self.rect.colliderect(rect2):
            self.setEstadoFINAL( valor, posicao)
            self.colisao = True
        else:
            self.colisao = False
    def getPosImagem(self):
        return self.posImagem

    def getRect(self):
        return self.rect

    def setRectTop(self, top):
        self.rect.top = top

    def set2RectTop(self, top):
        self.rect.top += top

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

    def getLucasAtual(self):
        return self.imagemBunoAtual

    def setEstadoFINAL(self,valor,posicao):
        if valor == 0:
            self.imagemBunoAtual =self.imagensDireita[posicao]
        if valor == 1:
            self.imagemBunoAtual =self.supresaInicial[posicao]
        if valor == 2:
            self.imagemBunoAtual =self.supresaFinal[posicao]
        if valor == 3:
            self.imagemBunoAtual =self.patinete[posicao]
        if valor == 4:
            self.imagemBunoAtual =self.andandoPatinete[posicao]
        if valor == 5:
            self.imagemBunoAtual =self.cama[posicao]





    def tipoImagem(self,valor):
        if valor == 0:
            self.imagemBunoAtual = self.imagensDireita[self.posImagem]
        if valor == 1:
            self.imagemBunoAtual =self.supresaInicial[self.posImagem]
        if valor == 2:
            self.imagemBunoAtual =self.supresaFinal[self.posImagem]
        if valor == 3:
            self.imagemBunoAtual =self.patinete[self.posImagem]
        if valor == 4:
            self.imagemBunoAtual =self.andandoPatinete[self.posImagem]
        if valor == 5:
            self.imagemBunoAtual =self.cama[self.posImagem]




    def EscolhaConjuntosImagens(self,valor):
        if valor == 0:
            return self.imagensDireita
        if valor == 1:
            return self.supresaInicial
        if valor == 2:
            return self.supresaFinal
        if valor == 3:
            return self.patinete
        if valor == 4:
            return self.andandoPatinete
        if valor == 5:
            return self.cama



    def atualizaIMagens(self,tempo,valor,tipo,escolha):   # troca a posicao do array lista do inimigo
      #  print('N1: %f' % (tempo) ,'------N2: %f' % (self.configTempo ) )


        if (self.configTempo) == ((tempo)):
                self.posImagem +=1;
                self.configTempo += valor
                if self.posImagem > len(self.EscolhaConjuntosImagens(escolha))-1:
                    self.posImagem = 0

        self.tipoImagem(tipo)


    def colocar(self, superficie):
        superficie.blit(self.imagemBunoAtual, self.rect)

