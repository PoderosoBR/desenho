import pygame,sys, os
from pygame.locals import *
import Abertura
import Personagem_LUCAS as Lucas
import Personagem_GUGU as GUGU
import Personagem_BUNO as BUNO
import ConfiguracaoDoTempo
import Acessorios
import Rotacao_Imagens as ROTACAO
import Balao


# configurações da tela ------------------------------------------------------------------------------------
pygame.init()                              # inicia o pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'     # mantem a tela no centro
largura = 1343                             # largura da tela
altura = 518                               # altura da tela
tempo1casaDECIMA = 0.06                    # criando uma variavel float que recebera o tempo do jogo
tela = pygame.display.set_mode((largura, altura))  # criando a tela com suas dimencoes
pygame.display.set_caption("OS BALULAS ")          # Titulo da tela
relogio = pygame.time.Clock()               # controla a velocidade dos fremes por segundo (HZ)
ImagemFundo = pygame.image.load('Imagem/Inicio.png')
ParaTUDO = False
# CONFIGURÇÂO DO PERSONAGENS-------------------------------------------------------------------------------------
#------------------ PERSONAGEM LUCAS E Abertura-----------------------------------------------------------------------
abertura = Abertura.Abertura(largura / 2, altura / 2)

lucas = Lucas.Lucas_Personagem(-200.0, 220.0)
ligaTempoLUCAS = 0
FramesLucas = 0.2  # velocidade que muda as imagens Lucas
veloLUCAS = 2
tipoImagemDoLUCAS = 0
posicaoEstadoFinaldeLucas = 0

#------------------ PERSONAGEM GUGU -----------------------------------------------------------------------
gugu = GUGU.Gugu_Personagem(-600.0, 220.0)
ligaTempoGUGU = 0
FramesGUGU = 0.5  # velocidade que muda as imagens Lucas
veloGUGU = 2
tipoImagemDoGUGU = 0
posicaoEstadoFinalde = 0


#------------------ PERSONAGEM BUNO -----------------------------------------------------------------------
buno = BUNO.Buno_Personagem(-300.0, 220.0)
ligaTempoBuno = 0
FramesBuno = 0.5  # velocidade que muda as imagens Lucas
veloBuno = 2
tipoImagemDoBuno = 0
posicaoEstadoFinalde = 0



#----------------------------------------------VERIAVEL TEMPO
t = ConfiguracaoDoTempo.ConfiguracaoDoTempo(-300.0, 220.0)
volumeTempo = 10
opcao = 0
atualizaPosicao = False

#-------------------------------------------------------------------------------------------------ROTACAO
rotacao = ROTACAO.Rotacao_Imagens(0, altura,'PersonagensBuno/AndaDireita/8.png' )

EngrenagemGRANDE = ROTACAO.Rotacao_Imagens(largura-160, altura/2 + 80,'Maquina/Grande.png' )
EngrenagemPEQUENA = ROTACAO.Rotacao_Imagens(largura-    50, altura/2 + 180,'Maquina/pequena.png'  )
fumacaMaquina = Acessorios.Acessorios(largura-150, 90  , tela)
lampada = Acessorios.Acessorios(largura-289, 77  , tela)
chamas = Acessorios.Acessorios(largura-289, 77  , tela)
chamas2 = Acessorios.Acessorios(largura-160, altura/2 + 50  , tela)


# ----------------------------------------------------------------------------------ACESSORIOS
acessorios = Acessorios.Acessorios(650, 390,tela)
balao = Balao.Balao(300 , 50, tela)

# CENARIOS ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
volume = 0,9
LigaConstantes2 = 0
LigaConstantes = 0
Capitulo = 0
cenario = 1
fala=1
tempoAtual = 0
i=7
pulaTempo=1

# AUDIO do DESENHO  NARRADOR---------------------------------------------------------------------------------------------------------------------------------

#---- AUDIO DO CAPITULO 0 ------------------------------------------------------------------------------------------
VozAbertura = pygame.mixer.Sound('Criancas/abertura.ogg')

ola = pygame.mixer.Sound('AUDIOS/Capitulo_0/1_ola.ogg')
ver_2 = pygame.mixer.Sound('AUDIOS/Capitulo_0/2_Vieram_ate_aq.ogg')
cade_3 = pygame.mixer.Sound('AUDIOS/Capitulo_0/3_cade.ogg')
chegada_4 = pygame.mixer.Sound('AUDIOS/Capitulo_0/4_chegada.ogg')

naoViu_5 = pygame.mixer.Sound('AUDIOS/Capitulo_0/5_naoViu.ogg')
chamarAtencao_6 = pygame.mixer.Sound('AUDIOS/Capitulo_0/6_chamarAtencao.ogg')
Ola_LUCAS_7 = pygame.mixer.Sound('AUDIOS/Capitulo_0/7_Ola_LUCAS.ogg')
Sabiam_8 = pygame.mixer.Sound('AUDIOS/Capitulo_0/8_Sabiam.ogg')
Adora_9 = pygame.mixer.Sound('AUDIOS/Capitulo_0/9_Adora.ogg')
podeDancar_10 = pygame.mixer.Sound('AUDIOS/Capitulo_0/10_podeDancar.ogg')
dancaBEM_11 = pygame.mixer.Sound('AUDIOS/Capitulo_0/11_dancaBEM.ogg')
MedizUmaCoisa_12 = pygame.mixer.Sound('AUDIOS/Capitulo_0/12_MedizUmaCoisa.ogg')

Vuando_13 = pygame.mixer.Sound('AUDIOS/Capitulo_0/13_Vuando.ogg')
Dinv_14 = pygame.mixer.Sound('AUDIOS/Capitulo_0/14_Dinv.ogg')
VerAlgumaCoisa_15 = pygame.mixer.Sound('AUDIOS/Capitulo_0/15_VerAlgumaCoisa.ogg')
MasEraGugu_16 = pygame.mixer.Sound('AUDIOS/Capitulo_0/16_MasEraGugu.ogg')
GUGUAdoraPatinete_17 = pygame.mixer.Sound('AUDIOS/Capitulo_0/17_GUGUAdoraPatinete.ogg')

apareceBRUNO_18 = pygame.mixer.Sound('AUDIOS/Capitulo_0/18_apareceBRUNO.ogg')
AdoroPATINETEdoGUGU_19 = pygame.mixer.Sound('AUDIOS/Capitulo_0/19_AdoroPATINETEdoGUGU.ogg')
tentaSUBIR_20 = pygame.mixer.Sound('AUDIOS/Capitulo_0/20_tentaSUBIR.ogg')
manja_21 = pygame.mixer.Sound('AUDIOS/Capitulo_0/21_manja.ogg')
SeFOI_22 = pygame.mixer.Sound('AUDIOS/Capitulo_0/22_SeFOI.ogg')


#----------AUDIO DO CAPITULO 1----------------------------------------------------------------------------------------------------
Macio_1 = pygame.mixer.Sound('AUDIOS/Capitulo_1/1_Macio.ogg')
trecoMaquina_2 = pygame.mixer.Sound('AUDIOS/Capitulo_1/2_trecoMaquina.ogg')

#CRianças ------------------------------------------------------------------------------------------
sim = pygame.mixer.Sound('Criancas/sim.ogg')
nao = pygame.mixer.Sound('Criancas/nao.ogg')
aqui = pygame.mixer.Sound('Criancas/12.ogg')

# Tom Sonoros ------------------------------------------------------------------------------------
maiconMusica = pygame.mixer.Sound('Efeitos_Sonoros/maiconMusica.ogg')
motoRapida = pygame.mixer.Sound('Efeitos_Sonoros/motoRapida.ogg')
sla = pygame.mixer.Sound('Efeitos_Sonoros/sla.ogg')
zumm = pygame.mixer.Sound('Efeitos_Sonoros/Z.ogg')
SUSTO = pygame.mixer.Sound('Efeitos_Sonoros/!.ogg')
jump = pygame.mixer.Sound('Efeitos_Sonoros/jump.ogg')
alarme = pygame.mixer.Sound('Efeitos_Sonoros/alarme.ogg')
explosao = pygame.mixer.Sound('Efeitos_Sonoros/explosao.ogg')


def Relogio (tempo):
    total_segs = int(tempo)

    horas = total_segs // 3600
    dias = horas // 86400

    segs_restantes = total_segs % 3600
    minutos = segs_restantes // 60
    segs_restantes_final = segs_restantes % 60

    if (horas >= 24):
        dias = int(horas / 24)
        horas = int(horas % 24)

    print(dias, "dias,", horas, "horas,", minutos, "minutos e", segs_restantes_final, "segundos.")


def atualizaTempo( tempo1casaDEcima,nome,frames,valor,tipo):
    global ligaTempoLUCAS

    if ligaTempoLUCAS == 0:
        nome.setConfigTempo( tempo1casaDEcima )  # Atualiza ConfigTempo do LUCAS que vai receber o tempo atual do Desenho em segundos
        nome.AumentaDiminui(tempo1casaDEcima, frames,valor,tipo)  # muda Imagem do lucas e configTempo do lucas




def atualizaPersonagem( tempo1casaDEcima,nome2,frames2,valor2,tipo2,nome,tipo,frames,velo,escolha):
    global ligaTempoLUCAS,rotacao

    if ligaTempoLUCAS == 0:
        nome.setConfigTempo( tempo1casaDEcima )  # Atualiza ConfigTempo do LUCAS que vai receber o tempo atual do Desenho em segundos
        nome2.setConfigTempo( tempo1casaDEcima )  # Atualiza ConfigTempo do LUCAS que vai receber o tempo atual do Desenho em segundos
        rotacao.setConfigTempo(tempo1casaDEcima)
        EngrenagemGRANDE.setConfigTempo(tempo1casaDEcima)
        EngrenagemPEQUENA.setConfigTempo(tempo1casaDEcima)

        ligaTempoLUCAS = 1  # Não permite que Atualize  ConfigTempo do LUCAS novamente
    else:
        nome2.AumentaDiminui(tempo1casaDEcima, frames2,valor2,tipo2)  # muda Imagem do lucas e configTempo do lucas

        nome.atualizaIMagens(tempo1casaDEcima, frames,tipo,escolha)  # muda Imagem do lucas e configTempo do lucas
        nome.andaDireita(velo)  # lucas Anda para direita

def atualizaPersonagem2( tempo1casaDEcima,nome2,frames2,valor2,tipo2,nome,tipo,frames,velo,escolha):
    global ligaTempoLUCAS

    if ligaTempoLUCAS == 0:
        nome.setConfigTempo( tempo1casaDEcima )  # Atualiza ConfigTempo do LUCAS que vai receber o tempo atual do Desenho em segundos
        nome2.setConfigTempo( tempo1casaDEcima )  # Atualiza ConfigTempo do LUCAS que vai receber o tempo atual do Desenho em segundos

        ligaTempoLUCAS = 1  # Não permite que Atualize  ConfigTempo do LUCAS novamente
    else:
        nome2.AumentaDiminui(tempo1casaDEcima, frames2,valor2,tipo2)  # muda Imagem do lucas e configTempo do lucas

        nome.atualizaIMagens(tempo1casaDEcima, frames,tipo,escolha)  # muda Imagem do lucas e configTempo do lucas
        nome.andaEsquerda(velo)  # lucas Anda para direita


def DESENHO():
    global cenario,ligaTempoLUCAS,fala , VozAbertura,tempoAtual,i,j,pulaTempo,tipoImagemDoLUCAS,RecebeValorDoPulaCena
    global TipoDeTempo,NovoValor,volumeTempo,opcao,Capitulo,ImagemFundo,ParaTUDO
    VozAbertura.play()

    while True:

        relogio.tick(60)   # velocidade do jogo
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == K_LEFT:
                    opcao=1
                    volumeTempo -=10
                if evento.key == K_RIGHT:
                    opcao=2
                    volumeTempo +=10
                if evento.key == K_DOWN:
                    opcao=0
                    atualizaPosicao = False

                if evento.key == K_SPACE:
                    ParaTUDO = True
                if evento.key == K_x:
                    ParaTUDO = False
                if evento.key == K_0:
                    volume -= 0.1
                    somFundo.set_volume(volume)

                if evento.key == K_9:
                    volume += 0.1
                    somFundo.set_volume(volume)

        if ParaTUDO == False :
            tempo = float ( (pygame.time.get_ticks()/1000) ) # FREMES MUDA A CADA SEGUNDO

            auxTEMPO = tempo * 10
            tempo1casaDECIMA = (int(auxTEMPO))
            tempo1casaDECIMA /= 10

            atualizaTempo(tempo1casaDECIMA, t, FramesLucas, volumeTempo, opcao)

           # print('tempo: %f'%(tempo1casaDECIMA) )
           # print("LUCAS:",(lucas.getRect()) )
           # print("GUGU:",(gugu.getRect()) )
            #print("BUNO:",(buno.getRect()) )

            #Relogio(tempo1casaDECIMA)
           # print('tempo: %f'%(pulaTempo) )
            print('GET: ',t.getNovoTempo())
          #  print('fala: ',fala)
           # print('GET: ',ligaTempoLUCAS)


            tela.blit(ImagemFundo,(0,0))                 # coloca na tela a imagem de fundo
            abertura.comportamento(tempo1casaDECIMA,tela)

            if(tempo1casaDECIMA > abertura.getConfigTempo() and pulaTempo!=1):
                    abertura.setTamanho(-1)

            if abertura.getTamanho() == -1  :  # Quando a tamanho a Imagem da ABERTURA for ZERO

            # Para Audio -----------------------------------------------------------------------------------------------
                if Capitulo == 0:
                    ImagemFundo = pygame.image.load('Imagem/Casa.png')


                    if cenario == 1:
                        if fala == 1 and t.getNovoTempo() > 14 :
                            ola.stop()
                            fala=2
                        if fala == 2 and t.getNovoTempo() > 16 :
                           sim.stop()
                           fala = 3

                        if fala == 3 and t.getNovoTempo() > 24 :
                           ver_2.stop()
                           fala = 4

                        if fala == 4 and t.getNovoTempo() > 27 :
                           sim.stop()
                           fala = 5


                        if fala == 5 and t.getNovoTempo() > 33 :
                           cade_3.stop()
                           fala = 6

                        if fala == 6 and t.getNovoTempo() > 36 :
                           nao.stop()
                           fala = 7

                        if fala == 7 and t.getNovoTempo() > 40 :
                           chegada_4.stop()
                           fala = 8

                        if fala == 8 and t.getNovoTempo() > 82:
                           chegada_4.stop()
                           fala = 14

                        if fala == 8 and t.getNovoTempo() > 65:
                           chegada_4.stop()
                           fala = 11
                    if cenario == 3:
                        if fala == 8 and t.getNovoTempo() > 57 :
                           naoViu_5.stop()
                           fala = 9

                        if fala == 9 and t.getNovoTempo() > 63 :
                           chamarAtencao_6.stop()
                           fala = 10

                        if fala == 10 and t.getNovoTempo() > 65 :
                           aqui.stop()
                           fala = 11
                    if cenario == 4:

                        if fala == 11 and t.getNovoTempo() > 72:
                            Sabiam_8.stop()
                            fala = 12

                        if fala == 12 and t.getNovoTempo() > 78:
                            Adora_9.stop()
                            fala = 13

                        if fala == 13 and t.getNovoTempo() > 82:
                            podeDancar_10.stop()
                            fala = 13.2

                        if fala == 13.2 and t.getNovoTempo() > 89:
                             maiconMusica.stop()
                             fala = 14
                    if cenario == 5 :
                        if fala == 14 and t.getNovoTempo() > 94:
                            dancaBEM_11.stop()
                            fala = 15

                        if fala == 15 and t.getNovoTempo() > 102:
                            MedizUmaCoisa_12.stop()
                            fala = 15.2

                        if fala == 15.2 and t.getNovoTempo() > 103:
                            sla.stop()
                            fala = 15.3

                        if fala == 15.3 and t.getNovoTempo() > 104:
                            sla.stop()
                            fala = 16
                    if cenario >= 6   :
                        if fala == 16 and t.getNovoTempo() > 110:
                            Vuando_13.stop()
                            fala = 17

                        if fala == 17 and t.getNovoTempo() > 115:
                            Dinv_14.stop()
                            fala = 18

                        if fala == 18 and t.getNovoTempo() > 120:
                            MasEraGugu_16.stop()
                            fala = 19

                        if fala == 19 and t.getNovoTempo() > 129:
                            MasEraGugu_16.stop()
                            fala = 20
                    if cenario >= 7:
                        if fala == 20 and t.getNovoTempo() >  137 :
                            apareceBRUNO_18.stop()
                            fala =20.2
                    if cenario >= 8:
                        if fala == 20.2 and t.getNovoTempo() >  138 :
                            SUSTO.stop()
                            fala =20.3


                        if fala == 20.3 and t.getNovoTempo() >  146:
                            zumm.stop()
                            fala = 21

                        if fala == 21 and t.getNovoTempo() >  155:
                            AdoroPATINETEdoGUGU_19.stop()
                            fala = 22

                        if fala == 22 and t.getNovoTempo() > 160:
                            tentaSUBIR_20.stop()
                            fala = 23
                    if cenario >= 10 :
                            if fala == 23 and  t.getNovoTempo() > 166:
                                SeFOI_22.stop()
                                fala=24
                if Capitulo == 1:
                    if cenario ==0 and t.getNovoTempo() > 182  :
                        fala = 25
                    if cenario == 1:
                        if fala ==25 and t.getNovoTempo() > 188:
                            Macio_1.stop()
                            fala = 26
                    if cenario == 2:
                        if fala == 26 and t.getNovoTempo > 254:
                            alarme.stop()
                            fala = 27


            #INICIA AUDIO----------------------------------------------------------------------------------INICIA AUDIO
                if Capitulo == 0:
                    fumacaMaquina.atualizaContantesDoCenario(tempo1casaDECIMA, 3, 0.3, 3)
                    lampada.atualizaContantesDoCenario(tempo1casaDECIMA, 4, 0.3, 4)
                    EngrenagemGRANDE.comportamento(tempo1casaDECIMA, tela, 0, 0, 0)
                    EngrenagemPEQUENA.comportamento(tempo1casaDECIMA, tela, 0, 0, 2)

                    if cenario == 1:
                            if fala == 1 and t.getNovoTempo() > 6 and t.getNovoTempo() <= 12:
                                ola.play()
                                fala = 2
                            elif fala == 2 and t.getNovoTempo() > 12 and t.getNovoTempo() <= 16:
                                sim.play()
                                fala = 3

                            elif fala == 3 and t.getNovoTempo() > 16 and t.getNovoTempo() <= 25:
                                ver_2.play()
                                fala = 4
                            elif fala == 4 and t.getNovoTempo() > 24 and t.getNovoTempo() <= 27:
                                sim.play()
                                fala = 5
                            elif fala == 5 and t.getNovoTempo() > 27 and t.getNovoTempo() <= 33:
                                cade_3.play()
                                fala = 6
                            elif fala == 6 and t.getNovoTempo() > 33 and t.getNovoTempo() < 36:
                                nao.play()
                                fala = 7
                            elif fala == 7 and t.getNovoTempo() > 36 and t.getNovoTempo() < 40:
                                chegada_4.play()
                                fala = 8

                            if lucas.getRectLeft() <= (largura/2-100) and t.getNovoTempo() >= 41 and t.getNovoTempo()  <= 49:
                                atualizaPersonagem(tempo1casaDECIMA, t, 1, volumeTempo, opcao,lucas,0,FramesLucas,veloLUCAS,0)
                            else:
                                lucas.setEstadoFINAL( tipoImagemDoLUCAS,0)
                                ligaTempoLUCAS = 0

                                if t.getNovoTempo() > 49: # verificar se cenario 1 foi feito

                                    lucas.setEstadoFINAL(tipoImagemDoLUCAS, 0)
                                    cenario=2
                                    lucas.setRectLeft(572)
                    if cenario == 2:

                            tipoImagemDoLUCAS=1
                            posicaoEstadoFinaldeLucas=0
                            if t.getNovoTempo() > 50 and t.getNovoTempo() <= 52:
                                atualizaPersonagem(tempo1casaDECIMA, t, 1, volumeTempo, opcao,lucas, 1, FramesLucas, 0, 1) # Olha para lados
                            else:
                                if t.getNovoTempo() > 52:             # pula para proxima
                                  lucas.setEstadoFINAL(1,0)
                                  cenario=3
                                  ligaTempoLUCAS = 0
                                  lucas.setRectLeft(572)
                    if cenario == 3:

                        if fala == 8 and t.getNovoTempo() > 52 and t.getNovoTempo() <= 57:
                            naoViu_5.play()
                            fala = 9

                        if fala == 9 and t.getNovoTempo() > 57 and t.getNovoTempo() <= 63:
                            chamarAtencao_6.play()
                            fala = 10

                        if fala == 10 and t.getNovoTempo() > 61 and t.getNovoTempo() <= 65:
                            aqui.play()
                            fala = 11

                        if t.getNovoTempo() >= 65 and t.getNovoTempo() < 67 : # Balanca o braco
                            tempoAtual = (int (tempo1casaDECIMA));
                            while  tempo1casaDECIMA == tempoAtual and i >= 0:
                                    lucas.setEstadoFINAL(2, i)
                                    tempoAtual+=1
                                    i-=1
                        else:
                            if t.getNovoTempo() >= 67:
                                cenario=4
                                ligaTempoLUCAS = 0
                                lucas.setEstadoFINAL(2, 0)
                                lucas.setRectLeft(572)
                    if cenario == 4:
                        tipoImagemDoLUCAS = 0
                        posicaoEstadoFinaldeLucas = 0

                        if fala == 11 and t.getNovoTempo() > 67 and t.getNovoTempo() <= 72:
                            Sabiam_8.play()
                            fala = 12

                        if fala == 12 and t.getNovoTempo() > 72 and t.getNovoTempo() <= 78:
                            Adora_9.play()
                            fala = 13

                        if fala == 13 and t.getNovoTempo() > 78 and t.getNovoTempo() <= 82:
                            podeDancar_10.play()
                            fala = 13.2

                        if fala == 13.2 and t.getNovoTempo() > 82 and t.getNovoTempo() <= 89:
                            maiconMusica.play()
                            fala = 14
                        if t.getNovoTempo() > 82 and t.getNovoTempo() < 89 :
                                atualizaPersonagem(tempo1casaDECIMA,t, 1, volumeTempo, opcao,lucas,3,FramesLucas,0,3) #DANÇA
                        else:
                             lucas.setEstadoFINAL(2, 0)  # posicao final da cena

                             if t.getNovoTempo() > 86:  # pula para proxima
                                cenario = 5
                                ligaTempoLUCAS = 0
                                lucas.setEstadoFINAL(2, 0)  # posicao final da cena
                                lucas.setRectLeft(572)
                    if cenario == 5:

                        if fala == 14 and t.getNovoTempo() > 91 and t.getNovoTempo() <= 94:
                            dancaBEM_11.play()
                            fala = 15

                        if fala == 15 and t.getNovoTempo() > 96 and t.getNovoTempo() <= 102:
                            MedizUmaCoisa_12.play()
                            fala = 15.2

                        if fala == 15.2 and t.getNovoTempo() > 102 and t.getNovoTempo() <= 103:
                            sla.play()
                            fala = 15.3

                        if  t.getNovoTempo() > 102 and t.getNovoTempo() <=103: # SEI LA-----------------
                           lucas.setEstadoFINAL(4,3)

                        if fala == 15.3 and t.getNovoTempo() > 103 and t.getNovoTempo() <= 104:
                            motoRapida.play()
                            fala = 16

                        if gugu.getRectLeft() <= (largura ) and t.getNovoTempo() > 104 :
                            atualizaPersonagem(tempo1casaDECIMA,t, FramesLucas, volumeTempo, opcao, gugu, 0, FramesGUGU, 100,0) # gugu lado Direito
                            lucas.verificaColisao(gugu.getRect(), 4, 0)

                        else:
                            ligaTempoLUCAS = 0

                            if t.getNovoTempo() > 104:  # verificar se cenario 1 foi feito
                                cenario = 6
                                gugu.setEstadoFINAL(0, 0)
                                lucas.setEstadoFINAL(4, 0)
                                lucas.setRectLeft(572)
                    if cenario == 6:
                        if fala == 16 and t.getNovoTempo() > 103 and t.getNovoTempo() <=110 :
                            Vuando_13.play()
                            fala = 17

                        if gugu.getRectLeft() > (-300) and t.getNovoTempo() > 110 and t.getNovoTempo() < 111: # gugu anda para esquerda
                                gugu.setEstadoFINAL(1, 0)
                                gugu.andaEsquerda(100)
                                lucas.verificaColisao(gugu.getRect(), 4, 1)

                        if fala == 17 and t.getNovoTempo() > 111 and t.getNovoTempo() <=115 :
                            Dinv_14.play()
                            fala = 18

                        if gugu.getRectLeft() < (largura/2+100) and t.getNovoTempo() > 115 and   t.getNovoTempo() < 120 : # anda de vagar GUGU
                            gugu.setEstadoFINAL(0, 0)
                            gugu.andaDireita(10)
                            acessorios.setEstadoFINAL(0, 6)

                            acessorios.verificaColisao(gugu.getRect(), 0, 0)
                            if acessorios.getColisao() == True:
                                lucas.setEstadoFINAL(4,0)
                        if fala == 18 and t.getNovoTempo() > 115 and t.getNovoTempo() < 120:
                            MasEraGugu_16.play()
                            fala = 18.2

                        if fala == 18.2 and t.getNovoTempo() > 115 and t.getNovoTempo() < 120: # som do patinete
                            motoRapida.play()
                            fala = 19

                        if gugu.getRectLeft() > (largura/2+100) and t.getNovoTempo() > 121 and t.getNovoTempo() <= 122:
                            gugu.setEstadoFINAL(2, 0)

                        if gugu.getRectLeft() > (largura / 2 + 100) and t.getNovoTempo() > 122 and t.getNovoTempo() <= 123:
                            gugu.setEstadoFINAL(2, 1)

                        if  fala == 19 and t.getNovoTempo() > 123 and  t.getNovoTempo() <= 129:
                            GUGUAdoraPatinete_17.play()
                            fala = 20

                        if  t.getNovoTempo() > 123:
                            cenario = 7
                            ligaTempoLUCAS = 0

                            lucas.setRectLeft(572)
                            gugu.setRectLeft(775)

                            gugu.setEstadoFINAL(2, 1)
                            lucas.setEstadoFINAL(4, 2)
                            acessorios.setRectLeft(1080)
                            acessorios.setRectTop(390)
                    if cenario == 7 :
                        if fala == 20 and t.getNovoTempo() > 130 and  t.getNovoTempo() <= 137 :
                            apareceBRUNO_18.play()
                            fala = 20.2

                        if  t.getNovoTempo() > 137  :
                                balao.setEstadoFINAL(0,5)

                        # CHEGA BRuNO
                        if buno.getRectLeft() <= (200) and t.getNovoTempo() > 129 and t.getNovoTempo() <= 137:
                            atualizaPersonagem(tempo1casaDECIMA, t, FramesBuno, volumeTempo, opcao, buno, 0, FramesBuno, 1, 0) # Bruno chega
                        else:
                            ligaTempoLUCAS = 0
                            if t.getNovoTempo() > 137:
                                buno.setEstadoFINAL(1, 0)
                                buno.setRectLeft(201)
                                gugu.setRectLeft(775)
                                lucas.setRectLeft(572)

                                cenario=8
                    if cenario == 8 :
                        if fala==20.2 and  t.getNovoTempo() > 137 and  t.getNovoTempo() <= 138:
                            SUSTO.play()
                            fala = 20.3


                        if fala == 20.3 and t.getNovoTempo() > 138 and t.getNovoTempo() <= 146:
                            zumm.play()
                            fala = 21

                        if buno.getRectLeft() > (200) and t.getNovoTempo() >= 138 and t.getNovoTempo() <= 146:
                            balao.setEstadoFINAL(0,0)
                            if(t.getNovoTempo()==138 or t.getNovoTempo()==141 or  t.getNovoTempo()==144 ):
                                buno.setRectLeft(600)
                                buno.setRectTop(220)
                                buno.setEstadoFINAL(2,0)

                            if (t.getNovoTempo() == 139 or t.getNovoTempo() == 142 or t.getNovoTempo() == 145 ):
                                buno.setRectLeft(800)
                                buno.setRectTop(300)
                                buno.setEstadoFINAL(2,1)

                            if (t.getNovoTempo() == 140 or t.getNovoTempo() == 143 or t.getNovoTempo() == 146 ):
                                buno.setRectLeft(900)
                                buno.setRectTop(220)
                                buno.setEstadoFINAL(2,2)

                        if fala == 21 and t.getNovoTempo() > 146 and t.getNovoTempo() <= 155:
                            AdoroPATINETEdoGUGU_19.play()
                            balao.setEstadoFINAL(0,6)
                            balao.setRectLeft(1050)
                            balao.setRectTop(100)
                            fala = 22

                        if fala == 22 and t.getNovoTempo() > 155 and t.getNovoTempo() <= 160:
                            balao.setEstadoFINAL(0,0)
                            tentaSUBIR_20.play()
                            fala = 23
                        else:
                            ligaTempoLUCAS = 0
                            if t.getNovoTempo() > 155:
                                lucas.setRectLeft(572)
                                gugu.setRectLeft(775)

                                cenario = 9
                    if cenario == 9 :
                            if t.getNovoTempo() >= 155 and t.getNovoTempo() <= 157:
                                    buno.setRectLeft(785)
                                    buno.setRectTop(210)
                                    buno.setEstadoFINAL(3, 0)
                                    gugu.setEstadoFINAL(2,2)

                            if t.getNovoTempo() > 160 and t.getNovoTempo() <= 161:
                                buno.setEstadoFINAL(3, 1)

                            else:
                                ligaTempoLUCAS = 0
                                if t.getNovoTempo() > 161:
                                    lucas.setRectLeft(572)
                                    gugu.setRectLeft(775)
                                    buno.setRectLeft(785)
                                    buno.setRectTop(210)
                                    cenario = 10
                    if cenario == 10 :
                            if fala == 23 and  t.getNovoTempo() >= 162 and t.getNovoTempo() <= 166:
                                SeFOI_22.play()
                                fala=24

                            if t.getNovoTempo() >= 163 and t.getNovoTempo() <= 166 and buno.getRectLeft() > (200):
                                    atualizaPersonagem2(tempo1casaDECIMA, t, FramesBuno, volumeTempo, opcao, buno, 4, FramesBuno,veloBuno, 4)  # Bruno chega

                            elif t.getNovoTempo() > 166 and t.getNovoTempo() <= 167.5 and buno.getRectLeft() < (910):
                                atualizaPersonagem(tempo1casaDECIMA, t, FramesBuno, volumeTempo, opcao, buno, 4, FramesBuno,10, 4)  # Bruno chega
                            else:
                                acessorios.verificaColisao(buno.getRect(),0,1)
                                buno.verificaColisao(acessorios.getRect(),3,2)
                                ligaTempoLUCAS = 0

                            if t.getNovoTempo() >=167.5 :
                                    buno.setEstadoFINAL(3,3)
                                    acessorios.setEstadoFINAL(0,2)
                                    acessorios.setRectLeft(916)
                                    acessorios.setRectTop(220)
                                    if buno.getRectLeft() < largura:
                                        buno.andaDireita(10)
                                        buno.set2RectTop(-10)
                                    else:
                                        acessorios.setEstadoFINAL(0, 3)

                            if t.getNovoTempo() > 172:
                                lucas.setRectLeft(572)
                                gugu.setRectLeft(775)

                                lucas.setEstadoFINAL(5,0)
                                gugu.setEstadoFINAL(4,0)
                                buno.setEstadoFINAL(5,2)

                                acessorios.setEstadoFINAL(0,0)
                                balao.setEstadoFINAL(0,0)

                                lampada.setEstadoFINAL(0,0)
                                fumacaMaquina.setEstadoFINAL(0,0)

                                cenario = 0
                                Capitulo = 1

                    fumacaMaquina.colocar(tela)  # mostrada o lucas na tela
                    lampada.colocar(tela)  # mostrada o lucas na tela
                    lucas.colocar(tela)  # mostrada o lucas na tela
                    gugu.colocar(tela)  # mostrada o lucas na tela
                    buno.colocar(tela)
                    acessorios.colocar(tela);
                    balao.colocar(tela);
                if Capitulo == 1 :
                    if cenario == 0 :
                        ImagemFundo = pygame.image.load('Imagem/FUNDO2.png')
                        tela.blit(ImagemFundo, (0, 0))

                        if fala == 24 and t.getNovoTempo() > 172 and t.getNovoTempo() <= 178   :
                            jump.play()
                            fala = 25

                        if rotacao.getRectLeft() < (400):
                            rotacao.comportamento(tempo1casaDECIMA, tela, 10, -5,0)

                        else:
                            if  rotacao.getRectTOP() <-100:
                                rotacao.comportamento(tempo1casaDECIMA, tela, 0, 0,0)
                              #  print(rotacao.getRectTOP())
                                cenario = 1
                                buno.setEstadoFINAL(5,0)
                                buno.setRectTop(0)
                                buno.setRectLeft(0)

                                acessorios.setEstadoFINAL(0,6)
                                acessorios.setRectTop(altura/2+150)
                                acessorios.setRectLeft(largura/2+300)
                            else:
                                rotacao.comportamento(tempo1casaDECIMA, tela, 10, -1,0)
                    if cenario == 1:
                        ImagemFundo = pygame.image.load('Imagem/cama.png')
                        tela.blit(ImagemFundo, (0, 0))

                        if(fala == 25 and t.getNovoTempo() > 182 and t.getNovoTempo() <= 188):
                            Macio_1.play()
                            fala= 26
                        if acessorios.getColisao() != True:
                            buno.andaDireita(5)
                            buno.set2RectTop(2)
                            acessorios.verificaColisao(buno.getRect(),0,6)
                            buno.setEstadoFINAL(5, 0)

                        else:
                            buno.setEstadoFINAL(5, 1)

                            buno.andaDireita(0)
                            buno.set2RectTop(0)

                            if t.getNovoTempo() > 189:
                                cenario = 2
                                buno.setEstadoFINAL(5,2)
                                ligaTempoLUCAS = 0
                    if cenario == 2:
                       if(fala == 26 and t.getNovoTempo() > 189 and t.getNovoTempo() <= 254):
                            alarme.play(10)
                            fala= 27

                        # FRASE ERRRO!!!!
                       if t.getNovoTempo() > 189 and t.getNovoTempo() <= 195.5 :
                            atualizaPersonagem(tempo1casaDECIMA, t, 1, volumeTempo, opcao, acessorios, 1, FramesLucas,0, 1)
                            acessorios.setRectLeft(0)
                            acessorios.setRectTop(0)

                       # FRASE TELA AZUL
                       if t.getNovoTempo() > 195.5:
                           atualizaPersonagem(tempo1casaDECIMA, t, 1, volumeTempo, opcao, acessorios, 2,FramesLucas, 0, 2)

                       if t.getNovoTempo() > 199.5:
                            cenario = 3
                            ligaTempoLUCAS= 0
                            acessorios.setEstadoFINAL(0,0)
                            lucas.setEstadoFINAL(4, 4)
                            lucas.setRectLeft(670)
                            lucas.setRectTop(220)

                            gugu.setEstadoFINAL(5, 0)
                            gugu.setRectLeft(775)
                            gugu.setRectTop(250)

                            acessorios.setEstadoFINAL(0, 3)
                            acessorios.setRectLeft(910)
                            acessorios.setRectTop(220)
                            lampada.setEstadoFINAL(5,1)
                    if cenario == 3 :
                        ImagemFundo = pygame.image.load('Imagem/CasaFinal.png')
                        alarme.set_volume(0.1)
                        tela.blit(ImagemFundo, (0, 0))

                        if (fala == 27 and t.getNovoTempo() > 200 and t.getNovoTempo() <= 207):
                            trecoMaquina_2.play()
                            fala = 28

                        if (fala == 28 and t.getNovoTempo() > 208 ):
                            alarme.stop()
                            explosao.play()
                            lampada.setEstadoFINAL(5,0)
                            gugu.setRectLeft(775)
                           # gugu.setRectTop(220)
                            fala = 29
                            cenario = 4
                        #    gugu.setEstadoFINAL(2, 2)
                    if cenario == 4 :
                        if t.getNovoTempo() > 220:
                          ImagemFundo = pygame.image.load('Imagem/fim.png')
                          tela.blit(ImagemFundo, (0, 0))

                    if t.getNovoTempo() > 210 and  t.getNovoTempo() <= 220:
                            chamas.atualizaContantesDoCenario(tempo1casaDECIMA, 6, 1, 6)
                            chamas2.atualizaContantesDoCenario(tempo1casaDECIMA, 7, 1, 7)



                    fumacaMaquina.colocar(tela)  # mostrada o lucas na tela
                    lampada.colocar(tela)  # mostrada o lucas na tela
                    lucas.colocar(tela)  # mostrada o lucas na tela
                    gugu.colocar(tela)  # mostrada o lucas na tela

                    buno.colocar(tela)
                    acessorios.colocar(tela);
                    balao.colocar(tela);
                    chamas.colocar(tela)  # mostrada o lucas na tela
                    chamas2.colocar(tela)  # mostrada o lucas na tela


        pygame.display.update()        #Atualiza o desenho com todas as mudanças
DESENHO()
