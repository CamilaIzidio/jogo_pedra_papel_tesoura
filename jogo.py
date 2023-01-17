###############################################################################
####          *********** PEDRA, PAPEL E TESOURA ***********               ####
###  O principal ponto treinado foi em relação à lógica de programação,     ###
###  estruturas de comparação e a utilização da biblioteca random do Python ###
###############################################################################

# Importando a biblioteca random para usar na escolha do computador
import random

# Classe para receber a escolha do jogador via teclado
def escolha_jogador():
    # Solicita a entrada do jogador e armazena na variável jogador
    jogador = input("Escolha: 'r' para pedra, 'p' para papel ou 't' para tesoura: ").lower()
    # Caso a jogada escolhida não seja uma das opções válidas ['r', 'p', 't'], retorna false
    if((jogador != 'r') and (jogador != 'p') and (jogador != 't')):
        return False
    # Caso a jogada escolhida seja uma das opções válidas ['r', 'p', 't'], retorna a escolha
    else:
        return jogador

# Classe para definir a escolha aleatória do computador
def escolha_computador():
    # Usando a biblioteca random e o método random.choice(possibilidades de escolhas),
    # é atribuído um valor entre ['r', 'p', 't'] para variável computador
    computador = random.choice(['r', 'p', 't'])
    # retornamos a escolha aleatória do computador
    return computador

# Classe para definir quem vence o jogo
def jogo():

    # chamando a classe que retorna a escolha do jogador e atribuindo o valor à variável jogador
    jogador = escolha_jogador()

    # chamando a classe que retorna a escolha do computador e atribuindo o valor à variável jogador
    computador = escolha_computador()

    # verifica se a escolha do jogador é válida
    if(jogador):
        # se as escolhas forem iguais
        if jogador == computador:
            print(f'Jogador {jogador} X {computador} Computador')
            return ('Empate!')
        # possíveis combinações para jogador vencer: r > t, t > p, p > r
        elif (jogador == 'r' and computador == 't') or (jogador == 't' and computador == 'p') or (jogador == 'p' and computador == 'r'):
            print(f'Jogador {jogador} X {computador} Computador')
            return ('Você venceu!')
        # caso contrário, computador vence
        else:
            print(f'Jogador {jogador} X {computador} Computador')
            return('Você perdeu!')

    # verifica se a escolha do jogador é válida, caso não seja, chama o mesmo método recursivamente
    else:
        print('Escolha inválida, escolha novamente!')
        jogo()
