def metodoBloqueioMovimento(x, y, mapaAtual, direcao, item_select):

    if x > -1 and x < 750 and y >-1 and y < 560:
        if mapaAtual == 1:
            if direcao == 'direita':
                if y < 330 and y > 200:
                    if (x+10>350 or x+10<270):
                        return True
                    else:
                        return False
                else:
                    return True
            if direcao == 'esquerda':
                if y < 330 and y > 200:
                    if (x-10>350 or x-10<270):
                        return True
                    else:
                        return False
                else:
                    return True
            if direcao == 'cima':
                if x > 250 and x < 350:
                    if (y-10<200 or y-10>310):
                        return True
                    else:
                        return False
                else:
                    return True

            if direcao == 'baixo':
                if x > 250 and x < 350:
                    if (y-10<200 or y-10>310):
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
            if item_select >=2 and direcao == 'cima':
                return True
            if item_select < 3 and direcao == 'baixo':
                return True
            else:
                return False
    else:
        return False