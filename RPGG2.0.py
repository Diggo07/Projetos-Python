# Importações
from time import *



# Variáveis
esclh = 2



# Programa Principal
print(' ')
print('         MENU')
print(' ')
sleep(2)



# Escolhas do Menu

while esclh == 2:
    print(' ')
    print('[ 1 ] - Jogar')
    print('[ 2 ] - Configurações')
    print('[ 3 ] - Sair')
    print(' ')

    esclh = int(input('Digite sua escolha: '))
    print(' ')
    sleep(2)

    if esclh == 1:
        print('Certo, vamos começar!')
        print(' ')
        sleep(2)

    elif esclh == 2:
        print('Ainda não temos as configurações')
        sleep(2)

    else:
        print('Saindo.')
        sleep(2)
        print('Saindo..')
        sleep(2)
        print('Saindo...')
        sleep(2)
        exit()



# Escolha de Modo

print('???? - Olá Jogador!')
sleep(2)
print('???? - Seja bem vindo ao mundo de RPGG')
sleep(2)
print('O que deseja jogar?')
print(' ')
print(' ')
sleep(2)

print('[ 1 ] - Single Player')
print('[ 2 ] - Duo Players')
print(' ')

esclh2 = int(input('Digite sua escolha: '))
sleep(2)

# Direção da escolha

if esclh2 == 1:
    print(' ')
    print('Certo Lobo solitário, vamos a criação do seu personagem!')
    print(' ')
    sleep(2)

# Nome do Jogador
    jgdr = input('Digite o nome do seu personagem: ')
    print(' ')
    sleep(2)

# Escolha da Raça
    print('Agora vamos a raça!')
    print(' ')
    sleep(1)

    print('[ 1 ] - Humano')
    print('[ 2 ] - Elfo')
    print('[ 3 ] - Meio-Humano')
    print('[ 4 ] - Demônio')
    print(' ')
    sleep(1)

    raca = int(input('Digite sua raça: '))
    sleep(2)

    if raca == 1:
        print('Certo Humano!')
        raca = 'Humano'
        sleep(2)

    elif raca == 2:
        print('Certo Elfo')
        raca = 'Elfo'
        sleep(2)

    elif raca == 3:
        print('Certo Meio Humano')
        raca = 'Meio Humano'
        sleep(2)
    
    elif raca == 4:
        print('Certo Demônio')
        raca = 'Demônio'
        sleep(2)

# Especialidades

    print(' ')
    print('Escolha sua especialidade!')
    print(' ')
    sleep(2)
    

    print('[ 1 ] - Magia')
    print('[ 2 ] - Combate Corpa a Corpo')
    print('[ 3 ] - Artilharia')
    print('[ 4 ] - Combate com arma branca')
    print(' ')
    sleep(2)

    espc = int(input('Digite sua especialidades: '))
    sleep(2)

    if espc == 1:
        print('Especialidade em Magia')
        espc = 'Magia'
        sleep(2)

    elif espc == 2:
        print('Especialidade em Combate Corpa a Corpo')
        espc = 'Combate Corpo a Corpo'
        sleep(2)
    
    elif espc == 3:
        print('Especialidade em Artilharia')
        espc = 'Artilharia'
        sleep(2)
    
    elif espc == 4:
        print('Especialidade em Combate com arma branca')
        espc = 'Combate com arma branca'
        sleep(2)

# Arma(s)

    print(' ')
    print('Agora escolha sua arma!')
    print(' ')
    sleep(2)

    print('[ 1 ] - Facas')
    print('[ 2 ] - Foice')
    print('[ 3 ] - Pistola(s)')
    print('[ 4 ] - Espada(s)')
    print('[ 5 ] - Arco e Flecha')
    print(' ')
    sleep(2)

    arma = int(input('Digite sua arma: '))
    sleep(2)

    if arma == 1:
        print('Faca escolhida')
        arma = 'Faca'
        sleep(2)

    elif arma == 2:
        print('Foice escolhida')
        arma = 'Foice'
        sleep(2)
    
    elif arma == 3:
        print('Pistola(s) escolhida')
        arma = 'Artilharia'
        sleep(2)
    
    elif espc == 4:
        print('Espada(s) escolhida')
        arma = 'Espada(s)'
        sleep(2)

    elif espc == 5:
        print('Arco e flecha escolhido')
        arma = 'Arco e flecha'
        sleep(2)

# Inicio da História

    print(' ')
    print('Seu personagem está pronto!')
    print(' ')
    sleep(2)
    print(f'Seu personagem acaba de spawnar na região\n central, ele se chama {jgdr}, \nele pertence a raça {raca}, possue sua habildidade \nem {espc}, lutando com {arma}')
    

#Modo Duo


else:
    print(' ')
    print('Certo aventureiros, vamos a criação de seus personagens!')
    print(' ')
    sleep(2)

# Nome jogador 1

    jgdr1 = input('Digite seu nome Jogador 1: ')
    print(f'Certo {jgdr1}!')
    print(' ')
    sleep(1)

# Nome jogador 2

    jgdr2 = input('Digite seu nome jogador 2: ')
    print(f'Certo {jgdr2}!')
    print(' ')
    sleep(1)

    print(f'Tudo certo então guerreiros {jgdr1} e {jgdr2}')

# Criação dos personagens

    print(f'Vamos criar seu personagem {jgdr1}!')
    print(' ')
    sleep(2)

#Raça do Jogador 1

    print('Agora vamos a raça!')
    print(' ')
    sleep(1)

    print('[ 1 ] - Humano')
    print('[ 2 ] - Elfo')
    print('[ 3 ] - Meio-Humano')
    print('[ 4 ] - Demônio')
    print(' ')
    sleep(1)

    raca1 = int(input('Digite sua raça: '))
    sleep(2)

    if raca1 == 1:
        print('Certo Humano!')
        raca1 = 'Humano'
        sleep(2)

    elif raca1 == 2:
        print('Certo Elfo')
        raca1 = 'Elfo'
        sleep(2)

    elif raca1 == 3:
        print('Certo Meio Humano')
        raca1 = 'Meio Humano'
        sleep(2)
    
    elif raca1 == 4:
        print('Certo Demônio')
        raca1 = 'Demônio'
        sleep(2)

# Especialidades do Jogador 1

    print(' ')
    print('Escolha sua especialidade!')
    print(' ')
    sleep(2)
    

    print('[ 1 ] - Magia')
    print('[ 2 ] - Combate Corpa a Corpo')
    print('[ 3 ] - Artilharia')
    print('[ 4 ] - Combate com arma branca')
    print(' ')
    sleep(2)

    espc1 = int(input('Digite sua especialidades: '))
    sleep(2)

    if espc1 == 1:
        print('Especialidade em Magia')
        espc1 = 'Magia'
        sleep(2)

    elif espc1 == 2:
        print('Especialidade em Combate Corpa a Corpo')
        espc1 = 'Combate Corpo a Corpo'
        sleep(2)
    
    elif espc1 == 3:
        print('Especialidade em Artilharia')
        espc1 = 'Artilharia'
        sleep(2)
    
    elif espc1 == 4:
        print('Especialidade em Combate com arma branca')
        espc1 = 'Combate com arma branca'
        sleep(2)

# Arma(s) do Jogador 1

    print(' ')
    print('Agora escolha sua arma!')
    print(' ')
    sleep(2)

    print('[ 1 ] - Facas')
    print('[ 2 ] - Foice')
    print('[ 3 ] - Pistola(s)')
    print('[ 4 ] - Espada(s)')
    print('[ 5 ] - Arco e Flecha')
    print(' ')
    sleep(2)

    arma1 = int(input('Digite sua arma: '))
    sleep(2)

    if arma1 == 1:
        print('Faca escolhida')
        arma1 = 'Faca'
        sleep(2)

    elif arma1 == 2:
        print('Foice escolhida')
        arma1 = 'Foice'
        sleep(2)
    
    elif arma1 == 3:
        print('Pistola(s) escolhida')
        arma1 = 'Artilharia'
        sleep(2)
    
    elif arma1 == 4:
        print('Espada(s) escolhida')
        arma1 = 'Espada(s)'
        sleep(2)

    elif arma1 == 5:
        print('Arco e flecha escolhido')
        arma1 = 'Arco e flecha'
        sleep(2)

# Jogador 2

    print(f'Vamos criar seu personagem {jgdr2}!')
    print(' ')
    sleep(2)

#Raça do Jogador 2

    print('Agora vamos a raça!')
    print(' ')
    sleep(1)

    print('[ 1 ] - Humano')
    print('[ 2 ] - Elfo')
    print('[ 3 ] - Meio-Humano')
    print('[ 4 ] - Demônio')
    print(' ')
    sleep(1)

    raca2 = int(input('Digite sua raça: '))
    sleep(2)

    if raca2 == 1:
        print('Certo Humano!')
        raca2 = 'Humano'
        sleep(2)

    elif raca2 == 2:
        print('Certo Elfo')
        raca2 = 'Elfo'
        sleep(2)

    elif raca2 == 3:
        print('Certo Meio Humano')
        raca2 = 'Meio Humano'
        sleep(2)
    
    elif raca2 == 4:
        print('Certo Demônio')
        raca2 = 'Demônio'
        sleep(2)

# Especialidades do Jogador 2

    print(' ')
    print('Escolha sua especialidade!')
    print(' ')
    sleep(2)
    

    print('[ 1 ] - Magia')
    print('[ 2 ] - Combate Corpa a Corpo')
    print('[ 3 ] - Artilharia')
    print('[ 4 ] - Combate com arma branca')
    print(' ')
    sleep(2)

    espc2 = int(input('Digite sua especialidades: '))
    sleep(2)

    if espc2 == 1:
        print('Especialidade em Magia')
        espc2 = 'Magia'
        sleep(2)

    elif espc2 == 2:
        print('Especialidade em Combate Corpa a Corpo')
        espc2 = 'Combate Corpo a Corpo'
        sleep(2)
    
    elif espc2 == 3:
        print('Especialidade em Artilharia')
        espc2 = 'Artilharia'
        sleep(2)
    
    elif espc2 == 4:
        print('Especialidade em Combate com arma branca')
        espc2 = 'Combate com arma branca'
        sleep(2)

# Arma(s) do Jogador 2

    print(' ')
    print('Agora escolha sua arma!')
    print(' ')
    sleep(2)

    print('[ 1 ] - Facas')
    print('[ 2 ] - Foice')
    print('[ 3 ] - Pistola(s)')
    print('[ 4 ] - Espada(s)')
    print('[ 5 ] - Arco e Flecha')
    print(' ')
    sleep(2)

    arma2 = int(input('Digite sua arma: '))
    sleep(2)

    if arma2 == 1:
        print('Faca escolhida')
        arma2 = 'Faca'
        sleep(2)

    elif arma2 == 2:
        print('Foice escolhida')
        arma2 = 'Foice'
        sleep(2)
    
    elif arma2 == 3:
        print('Pistola(s) escolhida')
        arma2 = 'Artilharia'
        sleep(2)
    
    elif arma2 == 4:
        print('Espada(s) escolhida')
        arma2 = 'Espada(s)'
        sleep(2)

    elif arma2 == 5:
        print('Arco e flecha escolhido')
        arma2 = 'Arco e flecha'
        sleep(2)

    print(' ')
    print('Seus personagens estão prontos!')
    print(' ')
    sleep(2)
    print(f'Seus personagens acabam de spawnar na região central')
    