import pygame,sys
from pygame.locals import *
import  Abertura
largura = 600
altura = 400
class Lucas_Personagem (pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagem1 = pygame.image.load('PersonagensLUCAS/AndaDireita/8.png')
        self.imagem2 = pygame.image.load('PersonagensLUCAS/AndaDireita/9.png')
        self.imagensDireita = [self.imagem1, self.imagem2 ] # lista de Imagem do inimigo

        self.imagemTRAS1 = pygame.image.load('PersonagensLUCAS/Tras/22.png')
        self.imagemTRAS2 = pygame.image.load('PersonagensLUCAS/Tras/31.png')
        self.imagemTRAS3 = pygame.image.load('PersonagensLUCAS/Tras/32.png')
        self.imagensTRAS = [self.imagemTRAS1 ,self.imagemTRAS2 , self.imagemTRAS3 ] # lista de Imagem do inimigo

        self.imagemTchau1 = pygame.image.load('PersonagensLUCAS/Frente/15.png')
        self.imagemTchau2 = pygame.image.load('PersonagensLUCAS/TCHAU/t1.png')
        self.imagemTchau3 = pygame.image.load('PersonagensLUCAS/TCHAU/2.png')
        self.imagemTchau4 = pygame.image.load('PersonagensLUCAS/TCHAU/3.png')
        self.imagemTchau5 = pygame.image.load('PersonagensLUCAS/TCHAU/4.png')
        self.imagemTchau6 = pygame.image.load('PersonagensLUCAS/TCHAU/5.png')
        self.imagemTchau7 = pygame.image.load('PersonagensLUCAS/TCHAU/6.png')
        self.imagemTchau8 = pygame.image.load('PersonagensLUCAS/TCHAU/7.png')
        self.imagemTchau9 = pygame.image.load('PersonagensLUCAS/TCHAU/8.png')

        self.imagemTchau = [self.imagemTchau1, self.imagemTchau2, self.imagemTchau3,
                            self.imagemTchau4, self.imagemTchau5, self.imagemTchau6,
                            self.imagemTchau7, self.imagemTchau8, self.imagemTchau9
                            ]

        self.imagemDanca1 = pygame.image.load('PersonagensLUCAS/Danca/1.png')
        self.imagemDanca2 = pygame.image.load('PersonagensLUCAS/Danca/2.png')
        self.imagemDanca3 = pygame.image.load('PersonagensLUCAS/Danca/3.png')
        self.imagemDanca4 = pygame.image.load('PersonagensLUCAS/Danca/4.png')
        self.imagemDanca5 = pygame.image.load('PersonagensLUCAS/Danca/5.png')
        self.imagemDanca6 = pygame.image.load('PersonagensLUCAS/Danca/6.png')
        self.imagemDanca7 = pygame.image.load('PersonagensLUCAS/Danca/7.png')
        self.imagemDanca8 = pygame.image.load('PersonagensLUCAS/Danca/8.png')

        self.imagemDanca = [self.imagemDanca1, self.imagemDanca2, self.imagemDanca3,
                            self.imagemDanca4, self.imagemDanca5, self.imagemDanca6,
                            self.imagemDanca7, self.imagemDanca8 ]

        self.imagemFrente1 = pygame.image.load('PersonagensLUCAS/Frente/F1.png')
        self.imagemFrente2 = pygame.image.load('PersonagensLUCAS/Frente/F2.png')
        self.imagemFrente3 = pygame.image.load('PersonagensLUCAS/Frente/15.png')
        self.imagemFrente4 = pygame.image.load('PersonagensLUCAS/Frente/sla.png')
        self.imagemFrente5 = pygame.image.load('PersonagensLUCAS/AndaDireita/12.png')

        self.imagemFrente = [self.imagemFrente1 ,self.imagemFrente2 , self.imagemFrente3 , self.imagemFrente4, self.imagemFrente5  ] # lista de Imagem do inimigo


        self.brancoX = pygame.image.load('PersonagensLUCAS/Branco.png')

        self.Branco = [self.brancoX ] # lista de Imagem do inimigo

        self.posImagem = 0 # variavel da posicao da lista de imagem do inimigo
        self.imagemLucasAtual = self.imagensDireita[self.posImagem] # cria image


        self.rect = self.imagemLucasAtual.get_rect()
        self.listaDisparo = []
        self.velocidade = 0.5
        self.rect.top = posy
        self.rect.left = posx
        self.configTempo = 0.0

    def setConfigTempo(self, configTempo ):
        self.configTempo = ( ( (( configTempo)) ))

    def verificaColisao(self,rect2,valor,posicao):                 # VERIFICA A COLISAO DO LUCAS COM OS OUTROS
        if self.rect.colliderect(rect2):
            self.setEstadoFINAL( valor, posicao)

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

    def getLucasAtual(self):
        return self.imagemLucasAtual

    def setEstadoFINAL(self,valor,posicao):
        if valor == 0:
            self.imagemLucasAtual =self.imagensDireita[posicao]
        if valor == 1:
            self.imagemLucasAtual =self.imagensTRAS[posicao]
        if valor == 2:
            self.imagemLucasAtual = self.imagemTchau[posicao]
        if valor == 3:
            self.imagemLucasAtual = self.imagemDanca[posicao]
        if valor == 4:
            self.imagemLucasAtual = self.imagemFrente[posicao]
        if valor == 5:
            self.imagemLucasAtual = self.Branco[posicao]

    def tipoImagem(self,valor):
        if valor == 0:
            self.imagemLucasAtual = self.imagensDireita[self.posImagem]
        if valor == 1:
            self.imagemLucasAtual = self.imagensTRAS[self.posImagem]
        if valor == 2:
            self.imagemLucasAtual = self.imagemTchau[self.posImagem]
        if valor == 3:
            self.imagemLucasAtual = self.imagemDanca[self.posImagem]
        if valor == 4:
            self.imagemLucasAtual = self.imagemFrente[self.posImagem]
        if valor == 5:
            self.imagemLucasAtual = self.Branco[self.posImagem]

    def EscolhaConjuntosImagens(self,valor):
        if valor == 0:
            return self.imagensDireita
        if valor == 1:
            return self.imagensTRAS
        if valor == 2:
            return self.imagemTchau
        if valor == 3:
            return self.imagemDanca
        if valor == 4:
            return self.imagemFrente
        if valor == 5:
            return self.Branco


    def atualizaIMagens(self,tempo,valor,tipo,escolha):   # troca a posicao do array lista do inimigo
      #  print('N1: %f' % (tempo) ,'------N2: %f' % (self.configTempo ) )


        if (self.configTempo) == ((tempo)):
                self.posImagem +=1;
                self.configTempo += valor
                if self.posImagem > len(self.EscolhaConjuntosImagens(escolha))-1:
                    self.posImagem = 0
        if (self.configTempo) < ((tempo)):
            self.configTempo = tempo
        self.tipoImagem(tipo)

        self.tipoImagem(tipo)


    def colocar(self, superficie):
        superficie.blit(self.imagemLucasAtual, self.rect)

