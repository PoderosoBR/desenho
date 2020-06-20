import pygame,sys
from pygame.locals import *
import  Abertura
largura = 600
altura = 400
class Balao (pygame.sprite.Sprite):
    def __init__(self,posx,posy,tela):
        pygame.sprite.Sprite.__init__(self)


        self.balao0 = pygame.image.load('BALAO/Branco.png')
        self.balao1 = pygame.image.load('BALAO/!.png')
        self.balao2 = pygame.image.load('BALAO/interogacao.png')
        self.balao3 = pygame.image.load('BALAO/interogacaoSEMnada.png')
        self.balao4 = pygame.image.load('BALAO/mantega.png')
        self.balao5 = pygame.image.load('BALAO/!!.png')
        self.balao6 = pygame.image.load('BALAO/coracao.png')


        self.balao = [ self.balao0, self.balao1 , self.balao2 , self.balao3 ,self.balao4  ,self.balao5 ,self.balao6 ]  # lista de Imagem do inimigo

        self.posImagem = 0 # variavel da posicao da lista de imagem do inimigo
        self.imagemAcessorioAtual = self.balao[self.posImagem] # cria image

        self.tela = tela
        self.rect = self.imagemAcessorioAtual.get_rect()
        self.listaDisparo = []
        self.velocidade = 0.5
        self.rect.top = posy
        self.rect.left = posx
        self.configTempo = 0.0
        self.colisao = False

    def setConfigTempo(self, configTempo ):
        self.configTempo = ( ( (( configTempo)) ))

    def verificaColisao(self,rect2,valor,posicao):                 # VERIFICA A COLISAO DO LUCAS COM OS OUTROS
        self.colisao = False
        if self.rect.colliderect(rect2):
            self.setEstadoFINAL( valor, posicao)
            self.colocar(self.tela)
            self.colisao = True
    def getColisao(self):
        return self.colisao

    def getPosImagem(self):
        return self.posImagem

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
        return self.imagemAcessorioAtual

    def setEstadoFINAL(self,valor,posicao):
        if valor == 0:
            self.imagemAcessorioAtual =self.balao[posicao]


    def tipoImagem(self,valor):
        if valor == 0:
            self.imagemAcessorioAtual = self.balao[self.posImagem]




    def EscolhaConjuntosImagens(self,valor):
        if valor == 0:
            return self.balao



    def atualizaIMagens(self,tempo,valor,tipo,escolha):   # troca a posicao do array lista do inimigo
      #  print('N1: %f' % (tempo) ,'------N2: %f' % (self.configTempo ) )


        if (self.configTempo) == ((tempo)):
                self.posImagem +=1;
                self.configTempo += valor
                if self.posImagem > len(self.EscolhaConjuntosImagens(escolha))-1:
                    self.posImagem = 0

        self.tipoImagem(tipo)


    def colocar(self, superficie):
        superficie.blit(self.imagemAcessorioAtual, self.rect)

