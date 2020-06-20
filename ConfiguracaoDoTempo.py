import pygame,sys
from pygame.locals import *
import  Abertura
largura = 600
altura = 400
class ConfiguracaoDoTempo (pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)


        self.configTempo = 0.0
        self.novoTempo = 0.0


    def setConfigTempo(self, configTempo ):
        self.configTempo = ( ( (( configTempo)) ))

    def getNovoTempo(self):
        return self.novoTempo

    def AumentaDiminui(self,tempo,frames,valor,tipo):   # troca a posicao do array lista do inimigo
       # print('NOVO: %f' % ((self.novoTempo )) ,'------CONF: %f' % (self.configTempo  ) )

        if (self.configTempo) == ((tempo)):
                self.configTempo += frames

                if tipo == 0:
                    self.novoTempo = self.configTempo

                if tipo == 1:

                    self.novoTempo = self.configTempo + valor

                if tipo == 2:
                    self.novoTempo = self.configTempo + valor



                if self.novoTempo < 0:
                    self.novoTempo = 0

    def andaTempo(self, tempo, frames):  # troca a posicao do array lista do inimigo
       # print('NOVO: %f' % ((self.novoTempo )) ,'------CONF: %f' % (self.configTempo  ) )

        if (self.configTempo) == ((tempo)):
            self.configTempo += frames
            self.novoTempo = self.configTempo

        if (self.configTempo) < ((tempo)):
            self.configTempo = tempo
        self.tipoImagem(tipo)

