#Menu do jogo
from time import sleep
sleep(1)

print('BEM VINDO AO RPGG')
sleep(1)

print('Entendeu a piada? HAHA "GG"... foi horrível vamos continuar')    #Piada com meu nome hahah
sleep(3)

print('Iniciando.') 
sleep(1)

print('Iniciando..')
sleep(1)

print('Iniciando...')
sleep(1)

#ÌNICIO

jogador1 = input('Qual será seu nome?: ')           #Nome do jogador

print(f'Olá {jogador1}!')

print('Deseja jogar em carreira SOLO ou DUO?')
                                                          #Modo de jogo
print(' ')
sleep(1)
print('       [ 1 ] - SOLO')
sleep(1)
print('       [ 2 ] - DUO')
sleep(1)
print(' ')
sleep(2)

mdj = int(input('Selecione um dos dois: '))

if mdj == 1:                                                        #Jogador1
    print('Então você é um lobo solitário? Hmm')
    print('Vamos começar...')

    print(f'Escolha sua arma {jogador1}!') 
    sleep(1)                                #Arma do Jogador1 em SOLO
    print(' ')
    print('[ 1 ] Espada')
    sleep(1)
    print('[ 2 ] Foice')
    sleep(1)
    print('[ 3 ] Arco e Flecha')
    sleep(1)
    print('[ 4 ] Cajado do Clérigo')
    sleep(1)
    print('[ 5 ] Machado')
    sleep(1)
    print('[ 6 ] Soco')
    sleep(1)
    print(' ')

    armaj1 = int(input('Qual será sua arma?: '))

    if armaj1 == 1:
        print('Você escolheu a "ESPADA"!')

    elif armaj1 == 2:
        print('Você escolheu a "FOICE"!')

    elif armaj1 == 3:
        print('Você escolheu o "ARCO E FLECHA"!')

    elif armaj1 == 4:
        print('Você escolheu a "CAJADO DO CLÉRIGO"!')

    elif armaj1 == 5:
        print('Você escolheu o "MACHADO"!')

    elif armaj1 == 6:
        print('Você escolheu ir no "SOCO"!')
        sleep(2)
    
    print('Opa')
    sleep(1)
    print('Opa')
    sleep(1)
    print(f'Opa esperem ai {jogador1} esse jogo está em beta!')
    print('Espero que tenha gostado da versão BETA (Mesmo q tenha sido pouca coisa) ')
    nota = input('Qual nota você dá pra ela? ')
    if 0 <= int(nota) <= 4 :
        print('Ok entâo... obrigado por jogar.')
    elif int(nota) == 5 :
        print('Acho que você gostou então, né?')
    elif 6<= int(nota) <= 9:
        print('Obrigadooooooo!!!! você me deixou muito feliz. ')
    elif int(nota) == 10:
        print('SÉRIOOOO?????? Nossa Obrigado mesmo você vai ser um dos primeiros a jogar <3!!!!!!!!')
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

elif mdj == 2:                                                      # Configurar o Jogador2 obs:se tiver
    jogador2 = input('Escolha o nome do 2ºJogador: ') 
    dupla = input('Qual será o nome da dupla?: ')
    print('Vamos começar...')
    print(' ')

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    print(f'Escolha sua arma {jogador1}!') 
    print(' ')

    sleep(1)                                #Arma do Jogador1 em DUO
    print(' ')
    print('[ 1 ] Espada')
    sleep(1)
    print('[ 2 ] Foice')
    sleep(1)
    print('[ 3 ] Arco e Flecha')
    sleep(1)
    print('[ 4 ] Cajado do Clérigo')
    sleep(1)
    print('[ 5 ] Machado')
    sleep(1)
    print('[ 6 ] Soco')
    sleep(1)
    print(' ')

    armaj1 = int(input('Qual será sua arma?: '))

    if armaj1 == 1:
        print('Você escolheu a "ESPADA"!')

    elif armaj1 == 2:
        print('Você escolheu a "FOICE"!')

    elif armaj1 == 3:
        print('Você escolheu o "ARCO E FLECHA"!')

    elif armaj1 == 4:
        print('Você escolheu a "CAJADO DO CLÉRIGO"!')

    elif armaj1 == 5:
        print('Você escolheu o "MACHADO"!')

    elif armaj1 == 6:
        print('Você escolheu ir no "SOCO"!')
        sleep(2)

                                                                    #Arma do Jogador2

    print(f'Escolha sua arma {jogador2}!')
    sleep(1)
    print(' ')
    print('[ 1 ] Espada')
    sleep(1)
    print('[ 2 ] Foice')
    sleep(1)
    print('[ 3 ] Arco e Flecha')
    sleep(1)
    print('[ 4 ] Cajado do Clérigo')
    sleep(1)
    print('[ 5 ] Machado')
    sleep(1)
    print('[ 6 ] Soco')
    sleep(1)
    print(' ')

    armaj2 = int(input('Qual será sua arma?: '))

    if armaj2 == 1:
        print('Você escolheu a "ESPADA"!')

    elif armaj2 == 2:
        print('Você escolheu a "FOICE"!')

    elif armaj2 == 3:
        print('Você escolheu o "ARCO E FLECHA"!')

    elif armaj2 == 4:
        print('Você escolheu a "CAJADO DO CLÉRIGO"!')

    elif armaj2 == 5:
        print('Você escolheu o "MACHADO"!')

    elif armaj2 == 6:
        print('Você escolheu ir no "SOCO"!')
        sleep(2)
    print('Opa')
    sleep(1)
    print('Opa')
    sleep(1)
    print(f'Opa esperem ai {dupla} esse jogo está em beta!')
    print('Espero que tenham gostado da versão BETA (Mesmo q tenha sido pouca coisa) ')
    nota = input('Qual nota vocês dão pra ela? ')
    if 0 <= int(nota) <= 4 :
        print('Ok entâo... obrigado por jogar.')
    elif int(nota) == 5 :
        print('Acho que vocês gostou então, né?')
    elif 6<= int(nota) <= 9:
        print('Obrigadooooooo!!!! vocês me deixou muito feliz. ')
    elif int(nota) == 10:
        print('SÉRIOOOO?????? Nossa Obrigado mesmo vocês vão ser um dos primeiros a jogar <3!!!!!!!!')