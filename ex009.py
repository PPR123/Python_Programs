import math
import time
import emoji
import random
print(emoji.emojize(":car:"*random.randint(30,35),use_aliases=True))
print("Criando um usuário para jogar adivinhação em Python")
print(emoji.emojize(":car:"*random.randint(30,35),use_aliases=True))
n = 0
pnome = str(input("Digite seu Primeiro nome: ")).upper()
nome = str(input("Digite seu Nome completo {}: ".format(pnome))).upper().strip()
name = nome.split()
print("Seu nome completo é {}".format(" ".join(name)))
first = nome.split()
print("Seu nome de login será : {} {}".format(first[0],first[-1]))
certo = str(input("Digite o nome de usuário, que você quer ser chamado: "))

print("PROCESSANDO",end="")
while n < 8:
    print("....",end="")
    time.sleep(1.5)
    n += 1
if len(certo) > len(nome):
    print( "DIgite um nome de usuário válido: ")
else:
    print(emoji.emojize("Usuário Cadastrado com sucesso: :thumbs_up:",use_aliases=True))
    time.sleep(2)
    import datetime
    data = datetime.date.today()
    print("-=-"*random.randint(30,35))
    print("Bem Vindo ao Jogo da adivinhação sua primeira vez jogando este jogo cemeçou hoje: {}".format(data))
    print("-=-"*random.randint(30,35))
    vezes = 2
    while vezes >= 1 :
        resp = random.randint(0,5)
        jogador = int(input("DIgite um número de 0 a 5: "))
        if jogador == resp:
            print("parabéns Você Ganhou")
            break
        else:
            vezes -= 1 
            print("Você Perdeu tente novamente. resta apenas {} tentativas".format(vezes))
