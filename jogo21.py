import baralho

def imprime(cartas):
    if cartas[0] == 1:
        return "A" + cartas[1]
    elif cartas[0] == 11:
        return "J" + cartas[1]
    elif cartas[0] == 12:
        return "Q" + cartas[1]
    elif cartas[0] == 13:
        return "K" + cartas[1]
    else:
        return str(cartas[0] + cartas[1])
    
def somaPontos(mao):
    pontos = 0
    for carta in mao:
        if carta in mao:
            if carta[0] > 10:
                pontos =+ 10
            else:
                pontos =+ carta[0]

def querCarta(mao):
    for c in mao:
        print(c)
    resp = input("Quer carta (s/n)?")
    if resp == 's':
        return True
    return False

def querCartaCpu(monte):
    if somaPontos(mao) < 16:
        return True
    else:
        return False

monte = baralho.cria()
baralho.embaralha(monte)

mao_jog = baralho.distribui(monte, 2)
mao_cpu = baralho.distribui(monte, 2)

while querCarta(mao_jog):
    c = baralho.compra(monte)
    mao_jog.append(c)


while querCarta(mao_cpu):
    c = baralho.compra(monte)
    mao_cpu.append(c)

pontos_hum = somaPontos(mao_jog)
pontos_cpu = somaPontos(mao_cpu)
if pontos_hum > 21:
    print("CPU Venceu!")
elif pontos_cpu > 21:
    print("Você ganhou!")
elif pontos_cpu >= pontos_hum:
    print("CPU Venceu!")
else:
    print("Você ganhou!")
