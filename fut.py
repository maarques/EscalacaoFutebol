def padronizarNome(nome):
    if len(nome)>8:
        nome = nome[:8]
    return nome

def padronizandoJogador(jogador):
    jogadorPadrao = jogador.split(' ')
    jogadorPadrao[0] = padronizarNome(jogadorPadrao[0])
    jogadorPadrao[2] = int(jogadorPadrao[2])
    return jogadorPadrao

def checkNome(nome, jogadoresNoTime):
    if nome in jogadoresNoTime:
        return True
    return False

def checkPosicao(posicao):
    padrao = ['goleiro', 'defensor', 'meia',  'atacante']
    if posicao not in padrao:
        return True
    return False

def checkHabilidade(habilidade):
    if habilidade > 10 or habilidade < 0:
        return True
    return False

def addJogador(jogador, lista):
    lista.append(jogador)
    return lista

def contratarJogador(jogador, Time, contador):
    if(jogador[1] == "goleiro"):
        Time[3].append((jogador[2],  contador, jogador[0], 'goleiro'))
        Time[3] = sorted(Time[3], key=lambda x: (-x[0], x[1]))
    if(jogador[1] == "defensor"):
        Time[2].append((jogador[2],  contador, jogador[0], 'defensor'))
        Time[2] = sorted(Time[2], key=lambda x: (-x[0], x[1]))
    if(jogador[1] == "meia"):
        Time[1].append((jogador[2],  contador, jogador[0], 'meia'))
        Time[1] = sorted(Time[1], key=lambda x: (-x[0], x[1]))
    if(jogador[1] == "atacante"):
        Time[0].append((jogador[2],  contador, jogador[0], "atacante"))
        Time[0] = sorted(Time[0], key=lambda x: (-x[0], x[1]))
    return Time

def contratar(jogador, jogadoresNoTime, Time, contador):
    if(checkNome(jogador[0].lower(), jogadoresNoTime)):
        print("Jogador já está no time")
        return jogadoresNoTime, Time, contador
    elif checkPosicao(jogador[1]):
        print('A posição informada não existe')
        return jogadoresNoTime, Time, contador
    elif checkHabilidade(jogador[2]):
        print('A habilidade do jogador deve estar entre 0 e 10')
        return jogadoresNoTime, Time, contador
    else:
        jogadoresNoTime = addJogador(jogador[0].lower(), jogadoresNoTime)
        Time = contratarJogador(jogador, Time, contador+1)
        return jogadoresNoTime, Time, contador+1


#trocar
def BuscarJogador(Time, nome):
    for x in Time:
        for y in x:
            if y[2].lower() == nome:
                return y

def checkJogador(jogador, Time,  jogadoresNoTime):
    if not checkNome(jogador[0].lower(), jogadoresNoTime):
        return True
    aux = BuscarJogador(Time, jogador[0].lower())
    if(jogador[2] != aux[0]):
        return True
    elif (jogador[1] != aux[3]):
        return True
    else:
        return False

def removerJogador(jogador, time):
    aux = BuscarJogador(Time, jogador[0].lower())
    if aux in time[0]:
        time[0].remove(aux)
    elif aux in time[1]:
        time[1].remove(aux)
    elif aux in time[2]:
        time[2].remove(aux)
    elif aux in time[3]:
        time[3].remove(aux)
    return time


def troca(jogadorAtual, jogadorSub, Time, jogadoresNoTime, contador):
    if(checkJogador(jogadorAtual, Time, jogadoresNoTime)):
        print("Jogador não está no time")
        return Time, jogadoresNoTime, contador
    elif checkNome(jogadorSub[0].lower(), jogadoresNoTime):
        print("Jogador já está no time")
        return Time, jogadoresNoTime, contador
    elif checkPosicao(jogadorSub[1]):
        print('A posição informada não existe')
        return Time, jogadoresNoTime, contador
    elif checkHabilidade(jogadorSub[2]):
        print('A habilidade do jogador deve estar entre 0 e 10')
        return Time, jogadoresNoTime, contador
    else:
        jogadoresNoTime.remove(jogadorAtual[0].lower())
        time = removerJogador(jogadorAtual, Time)
        jogadoresNoTime = addJogador(jogadorSub[0].lower(), jogadoresNoTime)
        Time = contratarJogador(jogadorSub, Time, contador+1)
        return Time, jogadoresNoTime, contador+1

#esquema
def checkEsquema(esquema):
    if sum(esquema) != 10:
        print("A soma das posições deve totalizar 10 jogadores")
        return False
    for x in esquema:
        if x > 4 or x < 2:
            print("Cada posição deve conter entre 2 e 4 jogadores")
            return False
    return True


#Time
def checkFormacao(Time, esquema):
    if(len(Time[3]) < 1):
        return False
    if(len(Time[2]) < esquema[0]):
        return False
    if(len(Time[1]) < esquema[1]):
        return False
    if(len(Time[0]) < esquema[2]):
        return False
    return True

def FaltaJogador(Time, esquema):
    print("Estão faltando jogadores no time:")
    if(len(Time[3]) < 1):
        print("1 goleiro")
    if(len(Time[2]) < esquema[0]):
        print(f"{esquema[0] - len(Time[2])} defensores")
    if(len(Time[1]) < esquema[1]):
        print(f"{esquema[1] - len(Time[1])} meias")
    if(len(Time[0]) < esquema[2]):
        print(f"{esquema[2] - len(Time[0])} atacantes")


def apresentarPossicao(jogadores, esquema):
    if(esquema == 2):
        print('|{:^20}{:^20}|'.format(jogadores[0][2], jogadores[1][2]))
        print(f"|{' ' * 9}o{' ' * 19}o{' ' * 10}|")
    if(esquema == 3):
        print("|{:^13}{:^13}{:^13} |".format(jogadores[0][2], jogadores[1][2],jogadores[2][2]))
        print(f"|{' ' * 5}o{' ' * 12}o{' ' * 12}o{' ' * 8}|")
    if(esquema == 4):
        print("|{:^10}{:^10}{:^10}{:^10}|".format(jogadores[0][2], jogadores[1][2],jogadores[2][2], jogadores[3][2]))
        print(f"|{' ' * 4}o{' ' * 9}o{' ' * 9}o{' ' * 9}o{' ' * 5}|")


def ApresentarTime(Time, esquema):
    inicio = ['+----------------------------------------+', '|              |          |              |', '|               ----------               |', '|                                        |']
    padrao = "|                                        |"
    for x in inicio:
        print(x)
    apresentarPossicao(Time[0], esquema[2])
    print(padrao)
    apresentarPossicao(Time[1], esquema[1])
    print("|                  (  )                  |")
    print(padrao)
    print(padrao)
    apresentarPossicao(Time[2], esquema[0])
    print(padrao)
    print("|               ----o-----               |")
    goleiro = Time[3][0]
    print("|              |{:^10}|              |".format(goleiro[2]))
    print('+----------------------------------------+')
    
def MontarTime(Time, Esquema):
    if(checkFormacao(Time, Esquema)):
        ApresentarTime(Time, Esquema)
    else:
        FaltaJogador(Time, Esquema)

def olharTime(time):
    for x in time:
        print(*x)
#main
Time = [[],[],[],[]]
jogadoresNoTime = []
execucao = True
EsquemaDefinido = False
Esquema = []
contador = 0


while execucao:
    op = int(input())
    if op == 1:
        jogador = input()
        jogador = padronizandoJogador(jogador)
        jogadoresNoTime, Time, contador = contratar(jogador, jogadoresNoTime, Time, contador)
    if op == 2:
        jogador = input().split(" x ")
        jogadorAtual = padronizandoJogador(jogador[0])
        jogadorSub = padronizandoJogador(jogador[1])
        Time, jogadoresNoTime, contador = troca(jogadorAtual, jogadorSub, Time, jogadoresNoTime, contador)
    if op == 3:
        aux = [int (x) for x in input().split(" ")]
        if checkEsquema(aux):
            Esquema = aux
            EsquemaDefinido = True
    if op == 4:
        if not EsquemaDefinido:
            print("O Esquema tático deve ser estabelecido antes de montar o time")
        else:
            MontarTime(Time, Esquema)
    if op == 5:
        execucao = False
