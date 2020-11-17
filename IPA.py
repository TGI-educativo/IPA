import pygame
pygame.init()
x = 400 #posição inicial personagem em x
y = 300 #posição inicial personagem em y
select_x = 530 #posição inicial icone de selecionar em x
select_y = 440 #posição inicial icone de selecionar em y
item_select = 1 #indice select inicial
modo_select = 1
modo_tela = 1
status_tela_pc = "off"
feedback_status = "off"
questionario_status = "off"
conteudo_status = "on"
quest_num = 1
direcao = ""
velocidade = 10
mapaAtual = 1
mapaAnterior = 0
num_questionario = 1
feed_num = 0
timer = 0
horas = 0
minutos = 0
segundos = 0
nivel_jogador = 1
exp_jogador = 0
exp_total = 0
nivel_conteudo = 1
questoes_respondidas = 0
questoes_corretas_total = 0
questoes_corretas_atual = 0
provas_feitas = 0
capa_ipa = pygame.image.load('graphics/capa-ipa.PNG')
instructions_box = pygame.image.load('graphics/instructions_box.PNG')
mapa1 = pygame.image.load('graphics/mapa_1.PNG')
mapa2 = pygame.image.load('graphics/mapa_2.PNG')
mapa3 = pygame.image.load('graphics/mapa_3.PNG')
mapa_info = pygame.image.load('graphics/info.PNG')
personagem_left1 = pygame.image.load('graphics/player_left1.PNG')
personagem_left2 = pygame.image.load('graphics/player_left2.PNG')
personagem_right1 = pygame.image.load('graphics/player_right1.PNG')
personagem_right2 = pygame.image.load('graphics/player_right2.PNG')
personagem_up1 = pygame.image.load('graphics/player_up1.PNG')
personagem_up2 = pygame.image.load('graphics/player_up2.PNG')
personagem_down1 = pygame.image.load('graphics/player_down1.PNG')
personagem_down2 = pygame.image.load('graphics/player_down2.PNG')
moca = pygame.image.load('graphics/moca.PNG')
moca = pygame.transform.scale(moca, [400, 200])
player_infobox = pygame.image.load('graphics/player_infobox.PNG')
select_op = pygame.image.load('graphics/select_op.PNG')
player_infobox = pygame.image.load('graphics/player_infobox.PNG')
infobox = pygame.image.load('graphics/infobox.PNG')
infobox = pygame.transform.scale(infobox, [500, 90])
select = pygame.image.load('graphics/select.PNG')
select = pygame.transform.scale(select, [50, 30])
barra = pygame.image.load('graphics/barra.png')
carregamento_original = pygame.image.load('graphics/carregamento.png')
carregamento = pygame.transform.scale(carregamento_original, [0, 30])
personagem = personagem_left1
primeira_entrada = pygame.image.load('graphics/houseoverworld.PNG')
primeira_entrada = pygame.transform.scale(primeira_entrada, [100, 100])
fonte1 = pygame.font.SysFont('arial black', 20)
fonte2 = pygame.font.SysFont('arial', 20)
text_selecionar = fonte1.render("Selecionar", True,(0,0,0))
text_equips = fonte1.render("Equips", True,(0,0,0))
text_sair = fonte1.render("Sair", True,(0,0,0))
selecione_um_personagem = fonte1.render("Selecione um personagem para iniciar", True,(255,255,255))
text_progresso = fonte1.render("Progresso: 1%", True,(255,165,0))
tela_pc = pygame.image.load('graphics/tela_pc.PNG')
tela_pc = pygame.transform.scale(tela_pc, [900,543])
labirinto = pygame.image.load('graphics/labirinto.PNG')
mapa6 =  pygame.image.load('graphics/mapa_6.PNG')
num_pag = 0
resposta_selecionada = ""
pagina_introducao = pygame.image.load('graphics/introducao_conteudo.PNG')
pagina1 = pygame.image.load('graphics/1-1.PNG')
pagina2 = pygame.image.load('graphics/1-2.PNG')
pagina3 = pygame.image.load('graphics/1-3.PNG')
pagina4 = pygame.image.load('graphics/1-4.PNG')
pagina5 = pygame.image.load('graphics/1-5.PNG')
pagina6 = pygame.image.load('graphics/1-6.PNG')
pagina7 = pygame.image.load('graphics/2-1.PNG')
pagina8 = pygame.image.load('graphics/2-2.PNG')
pagina9 = pygame.image.load('graphics/2-3.PNG')
pagina10 = pygame.image.load('graphics/2-4.PNG')
pagina11 = pygame.image.load('graphics/2-5.PNG')
pagina12 = pygame.image.load('graphics/2-6.PNG')
pagina13 = pygame.image.load('graphics/2-7.PNG')
pagina14 = pygame.image.load('graphics/2-8.PNG')
pagina15 = pygame.image.load('graphics/2-9.PNG')
#pagina16 = pygame.image.load('graphics/2-10.PNG')
#pagina17 = pygame.image.load('graphics/2-11.PNG')
pagina18 = pygame.image.load('graphics/3-1.PNG')
pagina19 = pygame.image.load('graphics/3-2.PNG')
pagina20 = pygame.image.load('graphics/3-3.PNG')
pagina21 = pygame.image.load('graphics/3-4.PNG')
pagina22 = pygame.image.load('graphics/3-5.PNG')
pagina23 = pygame.image.load('graphics/3-6.PNG')
pagina24 = pygame.image.load('graphics/3-7.PNG')
pagina25 = pygame.image.load('graphics/4-1.PNG')
pagina26 = pygame.image.load('graphics/4-2.PNG')
pagina27 = pygame.image.load('graphics/4-3.PNG')
pagina28 = pygame.image.load('graphics/4-4.PNG')
pagina29 = pygame.image.load('graphics/4-5.PNG')
#pagina30 = pygame.image.load('graphics/4-6.PNG')
pagina30 = pygame.image.load('graphics/4-7.PNG')
pagina31 = pygame.image.load('graphics/4-8.PNG')
pagina32 = pygame.image.load('graphics/4-9.PNG')
pagina33 = pygame.image.load('graphics/4-10.PNG')
pagina34 = pygame.image.load('graphics/4-11.PNG')
pagina35 = pygame.image.load('graphics/4-12.PNG')
pagina36 = pygame.image.load('graphics/4-13.PNG')
pagina37 = pygame.image.load('graphics/4-14.PNG')
pagina38 = pygame.image.load('graphics/4-15.PNG')
pagina39 = pygame.image.load('graphics/4-16.PNG')
pagina40 = pygame.image.load('graphics/4-17.PNG')
pagina41 = pygame.image.load('graphics/4-18.PNG')
pagina42 = pygame.image.load('graphics/5-1.PNG')
pagina43 = pygame.image.load('graphics/5-2.PNG')
pagina44 = pygame.image.load('graphics/5-3.PNG')
pagina45 = pygame.image.load('graphics/5-4.PNG')
pagina46 = pygame.image.load('graphics/5-5.PNG')
pagina47 = pygame.image.load('graphics/5-6.PNG')
pagina48 = pygame.image.load('graphics/5-7.PNG')
pagina49 = pygame.image.load('graphics/5-8.PNG')
questao1 = pygame.image.load('graphics/questao1.PNG')
questao2 = pygame.image.load('graphics/questao2.PNG')
questao3 = pygame.image.load('graphics/questao3.PNG')
questao4 = pygame.image.load('graphics/questao4.PNG')
questao5 = pygame.image.load('graphics/questao5.PNG')
questao6 = pygame.image.load('graphics/questao6.PNG')
questao7 = pygame.image.load('graphics/questao7.PNG')
questao8 = pygame.image.load('graphics/questao8.PNG')
questao9 = pygame.image.load('graphics/questao1.PNG')
questao10 = pygame.image.load('graphics/questao2.PNG')
questao11 = pygame.image.load('graphics/questao3.PNG')
questao12 = pygame.image.load('graphics/questao4.PNG')
questao13 = pygame.image.load('graphics/questao5.PNG')
questao14 = pygame.image.load('graphics/questao6.PNG')
questao15 = pygame.image.load('graphics/questao7.PNG')
questao16 = pygame.image.load('graphics/questao8.PNG')
questao17 = pygame.image.load('graphics/questao1.PNG')
questao18 = pygame.image.load('graphics/questao2.PNG')
questao19 = pygame.image.load('graphics/questao3.PNG')
questao20 = pygame.image.load('graphics/questao4.PNG')
questao21 = pygame.image.load('graphics/questao5.PNG')
questao22 = pygame.image.load('graphics/questao6.PNG')
questao23 = pygame.image.load('graphics/questao7.PNG')
questao24 = pygame.image.load('graphics/questao8.PNG')
questao25 = pygame.image.load('graphics/questao1.PNG')
questao26 = pygame.image.load('graphics/questao2.PNG')
questao27 = pygame.image.load('graphics/questao3.PNG')
questao28 = pygame.image.load('graphics/questao4.PNG')
questao29 = pygame.image.load('graphics/questao5.PNG')
questao30 = pygame.image.load('graphics/questao6.PNG')
questao31 = pygame.image.load('graphics/questao7.PNG')
questao32 = pygame.image.load('graphics/questao8.PNG')
questao33 = pygame.image.load('graphics/questao1.PNG')
questao34= pygame.image.load('graphics/questao2.PNG')
questao35 = pygame.image.load('graphics/questao3.PNG')
questao36 = pygame.image.load('graphics/questao4.PNG')
questao37 = pygame.image.load('graphics/questao5.PNG')
questao38 = pygame.image.load('graphics/questao6.PNG')
questao39 = pygame.image.load('graphics/questao7.PNG')
questao40 = pygame.image.load('graphics/questao8.PNG')
feedback_1_1 = pygame.image.load('graphics/feedback_1-1.PNG')
feedback_2_1 = pygame.image.load('graphics/feedback_2-1.PNG')
feedback_2_2 = pygame.image.load('graphics/feedback_2-2.PNG')
feedback_2_3 = pygame.image.load('graphics/feedback_2-3.PNG')
feedback_3_1 = pygame.image.load('graphics/feedback_3-1.PNG')
feedback_3_2 = pygame.image.load('graphics/feedback_3-2.PNG')
feedback_3_3 = pygame.image.load('graphics/feedback_3-3.PNG')
feedback_4_1 = pygame.image.load('graphics/feedback_4-1.PNG')
feedback_4_2 = pygame.image.load('graphics/feedback_4-2.PNG')
feedback_4_3 = pygame.image.load('graphics/feedback_4-3.PNG')
feedback_5_1 = pygame.image.load('graphics/feedback_5-1.PNG')
feedback_5_2 = pygame.image.load('graphics/feedback_5-2.PNG')
feedback_5_3 = pygame.image.load('graphics/feedback_5-3.PNG')
tipo_alternativa = 1

valor_progresso = 0






#Tamanho da janela de execução

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("IPA - Image Processing Adventure")


janela.blit(capa_ipa, (0,0))
modo_tela += 1
pygame.display.update()
pygame.time.delay(1) #original 4000

janela.blit(instructions_box, (0,0))
modo_tela += 1
pygame.display.update()
pygame.time.delay(4000)#original 4000

janela.blit(mapa1, (0,0))
janela.blit(player_infobox, (150,50))
modo_tela += 1
pygame.display.update()
pygame.time.delay(1)#8000

mapa_att = mapa1
respostas_corretas = [[1,'c'],
[2,'b'],
[3,'d'],
[4,'d'],
[5,'c'],
[6,'b'],
[7,'c'],
[8,'a'],
[9,'a'],
[10,'d'],
[11,'a'],
[12,'c'],
[13,'a'],
[14,'c'],
[15,'d'],
[16,'b'],
[17,'c'],
[18,'a'],
[19,'b'],
[20,'a'],
[21,'b'],
[22,'a'],
[23,'d'],
[24,'a'],
[25,'b'],
[26,'c'],
[27,'a'],
[28,'d'],
[29,'d'],
[30,'c']]



#metodo retorna verdadeiro ou falso se o personagem pode andar ou não

def metodoBloqueioMovimento(mapaAtual, direcao):

    if x > -1 and x < 750 and y >20 and y < 560:
        if mapaAtual == 1:
            if direcao == 'direita':
                if y < 330 and y > 200:
                    if (x+velocidade>350 or x+velocidade<270):
                        return True
                    else:
                        return False
                else:
                    return True
            if direcao == 'esquerda':
                if y < 330 and y > 200:
                    if (x-velocidade>350 or x-velocidade<270):
                        return True
                    else:
                        return False
                else:
                    return True
            if direcao == 'cima':
                if x > 250 and x < 350:
                    if (y-velocidade<200 or y-velocidade>310):
                        return True
                    else:
                        return False
                else:
                    return True

            if direcao == 'baixo':
                if x > 250 and x < 350:
                    if (y-velocidade<200 or y-velocidade>310):
                        return True
                    else:
                        return False
                else:
                    return True
        if mapaAtual == 2:
            if y<340 and y>210 and direcao != "direita" and x<400:
                if x> 130:
                    return True
                else:
                    return False
            if y<310 and y>180 and direcao != "esquerda" and x>400:
                if x< 550:
                    return True
                else:
                    return False
            else:
                return True
        if mapaAtual == 3:
            if status_tela_pc == "on":
                if item_select >= 2 and direcao == 'cima':
                    return True
                if item_select < 4 and direcao == 'baixo':
                    return True
                else:
                    return False
            if item_select >=2 and direcao == 'cima':
                return True
            if item_select < 3 and direcao == 'baixo':
                return True
            else:
                return False
        if mapaAtual == 5:
            if y >= 30 and y <= 100:
                if x >= 90 and x <= 180:
                    return True
                if x >= 480 and x <= 570:
                    return True
            if y>=110 and y<=130:
                if x >= 180 and x <= 210:
                    return True
                if x >= 450 and x <= 480:
                    return True
            if y>=140 and y<=160:
                if x >= 210 and x <= 240:
                    return True
                if x >= 420 and x <= 450:
                    return True
            if y>=170 and y<=190:#
                if x >= 240 and x <= 270:
                    return True
                if x >= 390 and x <= 420:
                    return True
            if y>=200 and y<=310:
                if x >= 270 and x <= 390:
                    return True
                if x >= 480 and x <= 580:
                    return True
            if y>=320 and y<=340:
                if x >= 240 and x <= 420:
                    return True
                if x >= 480 and x <= 580:
                    return True
            if y >= 350 and y <= 370:
                if x >= 210 and x <= 240:
                    return True
                if x >= 420 and x <= 450:
                    return True
            if y >= 380 and y <= 400:
                if x >= 180 and x <= 210:
                    return True
                if x >= 450 and x <= 480:
                    return True
            if y >= 410 and  y <= 520:
                if x >= 90 and x <= 180:
                    return True
                if x >= 480 and x <= 570:
                    return True
            else:
                return False
        if mapaAtual == 6:
            if x> 300 and x<360:
                return True
    else:
        return False
def verificaResposta(resposta,questao):

    if respostas_corretas[questao][1] == resposta:
        #somaVariavel_questãoCorreta_total e parcial
        return True
    else:
        return False






janela_aberta = True

while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    personagem = personagem_left2
    comandos = pygame.key.get_pressed()

    if mapaAtual != 3:
        if comandos[pygame.K_UP]:
            direcao = "cima"
            personagem = personagem_up2
            y -= velocidade
            if not(metodoBloqueioMovimento(mapaAtual, direcao)):
                y += velocidade
        if comandos[pygame.K_DOWN]:
            direcao = "baixo"
            personagem = personagem_down2
            y += velocidade
            if not(metodoBloqueioMovimento(mapaAtual, direcao)):
                y -= velocidade
        if comandos[pygame.K_LEFT]:
            direcao = "esquerda"
            personagem = personagem_left1
            x -= velocidade
            if not(metodoBloqueioMovimento(mapaAtual, direcao)):
                x += velocidade
        if comandos[pygame.K_RIGHT]:
            direcao = "direita"
            personagem = personagem_right1
            x += velocidade
            if not(metodoBloqueioMovimento(mapaAtual, direcao)):
                x -= velocidade
        if comandos[pygame.K_ESCAPE]:
            if mapaAtual != 4:
                mapaAnterior = mapaAtual
                mapaAtual = 4

            else:
                mapaAtual = mapaAnterior


    else:
        personagem = pygame.transform.scale(personagem_left2, [400, 200])
        if comandos[pygame.K_UP]:
            direcao = "cima"
            if (metodoBloqueioMovimento(mapaAtual, direcao)):
                item_select -= 1
                if modo_select == 1:
                    select_y -= 40
                elif modo_select == 2:
                    select_y -= 120
                elif modo_select == 3 and tipo_alternativa == 1:
                    select_y -= 30
                elif modo_select == 3 and tipo_alternativa == 2:
                    select_y -= 110
        if comandos[pygame.K_DOWN]:
            direcao = "baixo"
            if (metodoBloqueioMovimento(mapaAtual, direcao)):
                item_select += 1
                if modo_select == 1:
                    select_y += 40
                elif modo_select == 2:
                    select_y += 120
                elif modo_select == 3 and tipo_alternativa == 1:
                    select_y += 30
                elif modo_select == 3 and tipo_alternativa == 2:
                    select_y += 110

        if comandos[pygame.K_SPACE]:
            if item_select == 3 and modo_select == 1:
                personagem = personagem_left2
                mapa_att = mapa2
                mapaAtual = 2
                x = 80
                y = 360
            elif item_select == 1 and modo_select == 1:
                select_y = 100
                select_x = 50
                modo_select = 2
                item_select = 1

            elif modo_select == 2:
                status_tela_pc = "on"
                modo_select = 3
                select_y = 190
                select_x = 72
            if modo_select == 3 and tipo_alternativa == 2:
                item_select = 1
                select_y = 120
                select_x = 55

            elif modo_select == 3:
                if feedback_status != "on" and questionario_status != "on":
                    num_pag += 1
                    valor_progresso = valor_progresso +1

                pygame.time.delay(1000)

                if questionario_status == "on":
                    quest_num += 1


                if feedback_status == "on":
                    feed_num += 1
                    if num_questionario == 1:
                        if feed_num > 1:
                            feed_num = 2
                            num_pag = 7
                            feedback_status == "off"
                            questionario_status = "off"
                    if num_questionario == 2:
                        if feed_num > 4:
                            feed_num = 5
                            num_pag = 17
                            feedback_status == "off"
                            questionario_status = "off"
                    if num_questionario == 3:
                        if feed_num > 7:
                            feed_num = 8
                            num_pag = 26
                            feedback_status == "off"
                            questionario_status = "off"
                    if num_questionario == 4:
                        if feed_num > 10:
                            feed_num = 11
                            num_pag = 45
                            feedback_status == "off"
                            questionario_status = "off"
                    if num_questionario == 5:
                        if feed_num > 13:
                            feed_num = 14
                            feedback_status == "off"
                            questionario_status = "off"
                            status_tela_pc == "off"


                if num_pag > 54:
                    modo_select = 2
                    status_tela_pc = "off"
                    num_pag = 1


        if comandos[pygame.K_ESCAPE]:
            status_tela_pc = "off"
            select_x = 530
            select_y = 440
            item_select = 1
            modo_select = 1






    if x == 310 and y == 330 and mapaAtual != 2 and mapaAtual!= 5:
        mapa_att = mapa2
        mapaAtual = 2
        x = 320
        y = 540

    if x == 320 and y == 550 and mapaAtual != 1 and mapaAtual != 6:
        mapa_att = mapa1
        mapaAtual = 1
        x = 310
        y = 330

    if x == 80 and y == 340 and mapaAtual == 2:
        mapa_att = labirinto
        mapaAtual = 5
        x = 160
        y = 30
    if x == 320 and y == 30 and mapaAtual == 2:
        mapaAtual = 6
        x = 320
        y = 540

    if x == 120 and y == 40 and mapaAtual == 5:
        mapa_att = mapa2
        mapaAtual = 2
        x = 320
        y = 50
    if x == 320 and y == 550 and mapaAtual == 6:
        mapa_att = mapa1
        mapaAtual = 2
        x = 310
        y = 330
    if y < 200 and mapaAtual == 6:
        mapa_att = mapa3
        mapaAtual = 3
        x = 500
        y = 200

    janela.blit(mapa_att, (0, 0))

    if mapaAtual == 1:
        janela.blit(primeira_entrada, (320, 250))

    if mapaAtual == 3:
        janela.blit(select_op, (510, 430))
        if status_tela_pc == "off" or questionario_status == "on":
            janela.blit(select, (select_x, select_y))
        janela.blit(text_selecionar, (590, 440))
        janela.blit(text_equips, (590, 480))
        janela.blit(text_sair, (590, 520))
        if status_tela_pc != "on":
            janela.blit(moca, (-50,10))
            janela.blit(moca, (-50, 130))
            janela.blit(moca, (-50, 250))
            selecione_um_personagem = fonte1.render("Selecione um personagem para iniciar", True, (255, 255, 255))

        else:
            selecione_um_personagem = fonte1.render("Use a tecla 'espaço' para interagir", True, (255, 255, 255))


        janela.blit(infobox, (0,490))
        janela.blit(selecione_um_personagem, (20, 515))
        janela.blit(barra, (5, 430))
        tamanho_progresso = int(round(((476 / 54)*valor_progresso), 0)) #assim por algum motivo não ta funcionando mais
        text_progresso = fonte1.render("Progresso: "+str(round((100/54)*num_pag))+"%", True, (255, 165, 0))

        carregamento = pygame.transform.scale(carregamento_original, [tamanho_progresso, 30])
        janela.blit(carregamento, (16, 441))
        janela.blit(text_progresso, (160, 440))



        if status_tela_pc == "on":
            if num_pag == 0:
                tela_pc = pagina_introducao
            if num_pag == 1:
                num_questionario = 1
                tela_pc = pagina1

            if num_pag == 2:
                tela_pc = pagina2

            if num_pag == 3:
                tela_pc = pagina3

            if num_pag == 4:
                tela_pc = pagina4

            if num_pag == 5:
                tela_pc = pagina5

            if num_pag == 6:
                tela_pc = pagina6
                questionario_status = "on"
                feedback_status = "off"
                conteudo_status = "off"


            if num_pag == 7:
                num_questionario = 2

                questionario_status = "off"
                feedback_status = "off"
                conteudo_status = "on"
                tela_pc = pagina7
            if num_pag == 8:
                tela_pc = pagina8

            if num_pag == 9:
                tela_pc = pagina9

            if num_pag == 10:
                tela_pc = pagina10

            if num_pag == 11:
                tela_pc = pagina11

            if num_pag == 12:
                tela_pc = pagina12

            if num_pag == 13:
                tela_pc = pagina13

            if num_pag == 14:
                tela_pc = pagina14

            if num_pag == 15:
                tela_pc = pagina15


            if num_pag == 16:

                questionario_status = "on"
                feedback_status = "on"
                conteudo_status = "off"
            if num_pag == 17:

                questionario_status = "off"
                feedback_status = "off"
                conteudo_status = "on"
                num_pag = 18


            if num_pag == 18:

                num_questionario = 3
                tela_pc = pagina18
            if num_pag == 19:
                tela_pc = pagina19

            if num_pag == 20:
                tela_pc = pagina20

            if num_pag == 21:
                tela_pc = pagina21

            if num_pag == 22:
                tela_pc = pagina22

            if num_pag == 23:
                tela_pc = pagina23

            if num_pag == 24:
                tela_pc = pagina24




            if num_pag == 25:
                questionario_status = "on"
                feedback_status = "on"
                conteudo_status = "off"


            if num_pag == 26:
                questionario_status = "off"
                feedback_status = "off"
                conteudo_status = "on"
                num_pag = 27


            if num_pag == 27:
                num_questionario = 4
                tela_pc = pagina25

            if num_pag == 28:
                tela_pc = pagina26

            if num_pag == 29:
                tela_pc = pagina27

            if num_pag == 30:
                tela_pc = pagina28

            if num_pag == 31:
                tela_pc = pagina29

            if num_pag == 32:
                tela_pc = pagina30

            if num_pag == 33:
                tela_pc = pagina31

            if num_pag == 34:
                tela_pc = pagina32

            if num_pag == 35:
                tela_pc = pagina33

            if num_pag == 36:
                tela_pc = pagina34

            if num_pag == 37:
                tela_pc = pagina35

            if num_pag == 38:
                tela_pc = pagina36

            if num_pag == 39:
                tela_pc = pagina37

            if num_pag == 40:
                tela_pc = pagina38

            if num_pag == 41:
                tela_pc = pagina39

            if num_pag == 42:
                tela_pc = pagina40

            if num_pag == 43:
                tela_pc = pagina41



            if num_pag == 44:
                questionario_status = "on"
                feedback_status = "on"
                conteudo_status = "off"


            if num_pag == 45:
                questionario_status = "off"
                feedback_status = "off"
                conteudo_status = "on"
                num_pag = 46


            if num_pag == 46:
                num_questionario = 5
                tela_pc = pagina42

            if num_pag == 47:
                tela_pc = pagina43

            if num_pag == 48:
                tela_pc = pagina44

            if num_pag == 49:
                tela_pc = pagina45

            if num_pag == 50:
                tela_pc = pagina46

            if num_pag == 51:
                tela_pc = pagina47

            if num_pag == 52:
                tela_pc = pagina48

            if num_pag == 53:
                tela_pc = pagina49

            if num_pag == 54:
                questionario_status = "on"
                feedback_status = "on"
                conteudo_status = "off"



            if feedback_status == "on":
                if feed_num == 1:
                    tela_pc = feedback_1_1
                if feed_num == 2:
                    tela_pc = feedback_2_1
                if feed_num == 3:
                    tela_pc = feedback_2_2
                if feed_num == 4:
                    tela_pc = feedback_2_3
                if feed_num == 5:
                    tela_pc = feedback_3_1
                if feed_num == 6:
                    tela_pc = feedback_3_2
                if feed_num == 7:
                    tela_pc = feedback_3_3
                if feed_num == 8:
                    tela_pc = feedback_4_1
                if feed_num == 9:
                    tela_pc = feedback_4_2
                if feed_num == 10:
                    tela_pc = feedback_4_3
                if feed_num == 11:
                    tela_pc = feedback_5_1
                if feed_num == 12:
                    tela_pc = feedback_5_2
                if feed_num == 13:
                    tela_pc = feedback_5_3
                    questionario_status = "on"
                    feedback_status = "on"
                    conteudo_status = "off"

            if questionario_status == "on":
                if quest_num == 1:
                    tela_pc = questao1
                    tipo_alternativa = 1
                if quest_num == 2:
                    tela_pc = questao2
                    tipo_alternativa = 2
                if quest_num == 3:
                    tela_pc = questao3
                if quest_num == 4:
                    tela_pc = questao4
                if quest_num == 5:
                    tela_pc = questao5
                if quest_num == 6:
                    tela_pc = questao6
                if quest_num == 7:
                    tela_pc = questao7
                if quest_num == 8:
                    tela_pc = questao8
                if quest_num == 9:
                    tela_pc = feedback_1_1
                    questionario_status = "off"
                    feedback_status = "on"
                    conteudo_status = "off"


            janela.blit(tela_pc, (0, 0))
            if feedback_status == "on":
                txt = fonte2.render(str(questoes_corretas_atual), True, (0, 0, 0))
                janela.blit(txt, (245, 101))
                txt = fonte2.render(str(100*questoes_corretas_atual), True, (0, 0, 0))
                janela.blit(txt, (200, 120))
            if status_tela_pc == "off" or questionario_status == "on":
                janela.blit(select, (select_x, select_y))





    if timer < 20:
        timer+= 1
    else:
        timer = 0
        segundos += 1
        if segundos == 60:
            minutos += 1
            segundos = 0
            if minutos == 60:
                horas += 1
                minutos = 0

    tempo_str = "Tempo de jogo: "

    if horas < 10:
        tempo_str +="0"+ str(horas) + "h "
    else:
        tempo_str += str(horas) + "h "

    if minutos < 10:
        tempo_str +="0"+ str(minutos) + "m "
    else:
        tempo_str += str(minutos) + "m "

    if segundos < 10:
        tempo_str +="0"+ str(segundos) + "s"
    else:
        tempo_str += str(segundos) + "s"




    relogio = fonte1.render(tempo_str, True, (255, 255, 255))

    if mapaAtual == 4:
        janela.blit(mapa_info, (0, 0))
        text_nivel = fonte1.render("Nível jogador: " + str(nivel_jogador), True, (255, 255, 255))
        janela.blit(text_nivel, (350, 130))
        xp_restante = fonte1.render("Exp. para próximo nível: " + str(1000 - exp_jogador), True, (255, 255, 255))
        janela.blit(xp_restante, (350, 200))
        nivel_conteudo_txt = fonte1.render("Nível conteúdo: " + str(nivel_conteudo), True, (255, 255, 255))
        janela.blit(nivel_conteudo_txt, (350, 270))
        questoes_respondidas_txt = fonte1.render("Questões respondidas: " + str(questoes_respondidas), True, (255, 255, 255))
        janela.blit(questoes_respondidas_txt, (350, 340))
        provas_feitas_txt = fonte1.render("Questões respondidas: " + str(questoes_respondidas), True, (255, 255, 255))
        janela.blit(provas_feitas_txt, (350, 410))
        janela.blit(relogio, (350, 480))




    if mapaAtual == 5:
        janela.blit(labirinto, (0,0))
    if mapaAtual == 6:
        janela.blit(mapa6, (0,0))

    if mapaAtual!= 4 and status_tela_pc == "off":
        janela.blit(personagem, (x, y))
        #janela.blit(personagem, (320,30)) #personagem exemplo posição

    posicao_real = fonte1.render(("x: " + str(x) +" y: "+str(y) + "pagina atual:" + str(num_pag)), True, (255, 255, 255)) #posição do personagem
    janela.blit(posicao_real, (10,10))

    #pygame.draw.circle(janela, (0,255,0), (100,380),10)


    pygame.display.update()


pygame.quit()