import pygame,sys
from pygame.locals import *
import  Abertura
largura = 600
altura = 400
class Acessorios (pygame.sprite.Sprite):
    def __init__(self,posx,posy,tela):
        pygame.sprite.Sprite.__init__(self)

        self.acessorio0 = pygame.image.load('ACESSORIOS/Branco.png')
        self.acessorio1 = pygame.image.load('ACESSORIOS/batida.png')
        self.acessorio2 = pygame.image.load('ACESSORIOS/batePatinete.png')
        self.acessorio3 = pygame.image.load('ACESSORIOS/patineteQuebrado.png')
        self.acessorio4 = pygame.image.load('ACESSORIOS/mira.png')
        self.acessorio5 = pygame.image.load('ACESSORIOS/rosa.png')
        self.acessorio6 = pygame.image.load('ACESSORIOS/brancoPEQUENO.png')
        self.acessorio7 = pygame.image.load('ACESSORIOS/mira.png')

        self.acessorios = [self.acessorio0 ,self.acessorio1 ,  self.acessorio2 ,  self.acessorio3,self.acessorio4,
                           self.acessorio5,self.acessorio6,self.acessorio7 ]  # lista de Imagem do inimigo

        self.pc0 = pygame.image.load('Imagem/pc/1.png')
        self.pc1 = pygame.image.load('Imagem/pc/2.png')
        self.pc2 = pygame.image.load('Imagem/pc/3.png')
        self.pc3 = pygame.image.load('Imagem/pc/4.png')
        self.pc4 = pygame.image.load('Imagem/pc/5.png')
        self.pc5 = pygame.image.load('Imagem/pc/6.png')
        self.pc6 = pygame.image.load('Imagem/pc/7.png')

        self.pc = [self.pc0, self.pc1 , self.pc2 , self.pc3 ,self.pc4, self.pc5, self.pc6 ]  # lista de Imagem do inimigo



        self.azul0 = pygame.image.load('Imagem/pc/10.png')
        self.azul1 = pygame.image.load('Imagem/pc/11.png')
        self.azul2 = pygame.image.load('Imagem/pc/12.png')
        self.azul3 = pygame.image.load('Imagem/pc/13.png')
        self.azul4 = pygame.image.load('Imagem/pc/14.png')
        self.azul5 = pygame.image.load('Imagem/pc/15.png')
        self.azul6 = pygame.image.load('Imagem/pc/16.png')
        self.azul7 = pygame.image.load('Imagem/pc/17.png')


        self.azul = [self.azul0, self.azul1 , self.azul2 , self.azul3 ,self.azul4, self.azul5, self.azul6,self.azul7 ]  # lista de Imagem do inimigo

        self.chamine0 = pygame.image.load('Maquina/Chamine/outras/1.png')
        self.chamine1 = pygame.image.load('Maquina/Chamine/outras/2.png')
        self.chamine2 = pygame.image.load('Maquina/Chamine/outras/3.png')
        self.chamine3 = pygame.image.load('Maquina/Chamine/outras/4.png')
        self.chamine4 = pygame.image.load('Maquina/Chamine/outras/5.png')
        self.chamine5 = pygame.image.load('Maquina/Chamine/outras/6.png')
        self.chamine6 = pygame.image.load('Maquina/Chamine/outras/7.png')
        self.chamine7 = pygame.image.load('Maquina/Chamine/outras/8.png')

        self.chamine = [self.chamine0, self.chamine1, self.chamine2, self.chamine3, self.chamine4, self.chamine5, self.chamine6,
                     self.chamine7 ]  # lista de Imagem do inimigo

        self.lampada0 = pygame.image.load('Maquina/Lampada/1.png')
        self.lampada1 = pygame.image.load('Maquina/Lampada/2.png')

        self.lampada = [self.lampada0, self.lampada1]  # lista de Imagem do inimigo

        self.lampadaQuebrada0 = pygame.image.load('Maquina/Lampada/Quebrada.png')
        self.lampadaQuebrada1 = pygame.image.load('Maquina/Lampada/1.png')

        self.lampadaQuebrada = [self.lampadaQuebrada0, self.lampadaQuebrada1]  # lista de Imagem do inimigo

        self.chamas0 = pygame.image.load('Maquina/Chamas/1.png')
        self.chamas1 = pygame.image.load('Maquina/Chamas/2.png')
        self.chamas2 = pygame.image.load('Maquina/Chamas/3.png')
        self.chamas3 = pygame.image.load('Maquina/Chamas/4.png')

        self.chamas = [self.chamas0,self.chamas1,self.chamas2,self.chamas3 ]  # lista de Imagem do inimigo

        self.chamasOutra0 = pygame.image.load('Maquina/Chamas/8.png')
        self.chamasOutra1 = pygame.image.load('Maquina/Chamas/9.png')
        self.chamasOutra2 = pygame.image.load('Maquina/Chamas/10.png')
        self.chamasOutra3 = pygame.image.load('Maquina/Chamas/11.png')

        self.chamasOutra = [self.chamasOutra0, self.chamasOutra1, self.chamasOutra2, self.chamasOutra3]  # lista de Imagem do inimigo

        self.posImagem = 0 # variavel da posicao da lista de imagem do inimigo
        self.imagemAcessorioAtual = self.acessorios[self.posImagem] # cria image

        self.tela = tela
        self.rect = self.imagemAcessorioAtual.get_rect()
        self.listaDisparo = []
        self.velocidade = 0.5
        self.rect.top = posy
        self.rect.left = posx
        self.configTempo = 0.0
        self.colisao = False
        self.ligaConstante = 0

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

    def setConstante(self, valor):
        self.ligaConstante = valor

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

    def atualizaContantesDoCenario(self, tempo, tipo, frames, escolha):
        if self.ligaConstante == 0:
            self.setConfigTempo(tempo)  # Atualiza ConfigTempo do LUCAS que vai receber o tempo atual do Desenho em segundos

            self.ligaConstante = 1  # Não permite que Atualize  ConfigTempo do LUCAS novamente
        else:
            self.atualizaIMagens(tempo, frames, tipo, escolha)  # muda Imagem do lucas e configTempo do lucas

    def setEstadoFINAL(self,valor,posicao):
        if valor == 0:
            self.imagemAcessorioAtual =self.acessorios[posicao]
        if valor == 1:
            self.imagemAcessorioAtual =self.pc[posicao]
        if valor == 2:
            self.imagemAcessorioAtual =self.azul[posicao]
        if valor == 3:
            self.imagemAcessorioAtual =self.chamine[posicao]
        if valor == 4:
            self.imagemAcessorioAtual =self.lampada[posicao]
        if valor == 5:
            self.imagemAcessorioAtual =self.lampadaQuebrada[posicao]
        if valor == 6:
            self.imagemAcessorioAtual =self.chamas[posicao]
        if valor == 7:
            self.imagemAcessorioAtual =self.chamasOutra[posicao]



    def tipoImagem(self,valor):
        if valor == 0:
            self.imagemAcessorioAtual = self.acessorios[self.posImagem]
        if valor == 1:
            self.imagemAcessorioAtual = self.pc[self.posImagem]
        if valor == 2:
            self.imagemAcessorioAtual = self.azul[self.posImagem]
        if valor == 3:
            self.imagemAcessorioAtual = self.chamine[self.posImagem]
        if valor == 4:
            self.imagemAcessorioAtual = self.lampada[self.posImagem]
        if valor == 5:
            self.imagemAcessorioAtual = self.lampadaQuebrada[self.posImagem]
        if valor == 6:
            self.imagemAcessorioAtual = self.chamas[self.posImagem]
        if valor == 7:
            self.imagemAcessorioAtual = self.chamasOutra[self.posImagem]



    def EscolhaConjuntosImagens(self,valor):
        if valor == 0:
            return self.acessorios
        if valor == 1:
            return self.pc
        if valor == 2:
            return self.azul
        if valor == 3:
            return self.chamine
        if valor == 4:
            return self.lampada
        if valor == 5:
            return self.lampadaQuebrada
        if valor == 6:
            return self.chamas
        if valor == 7:
            return self.chamasOutra





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
        superficie.blit(self.imagemAcessorioAtual, self.rect)

