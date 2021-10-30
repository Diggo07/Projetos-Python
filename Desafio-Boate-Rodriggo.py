from time import sleep

print(' ')
print(' ')

print('                             \033[1;35;40mClub GG\033[m')                                #Nome da Boate
sleep(2)
print(' ')
print(' ')

print('Chegando no estabelecimento.')
sleep(1)
print('Chegando no estabelecimento..')              #início
sleep(1)
print('Chegando no estabelecimento...')
sleep(1)
print(' ')
print('Você chegou!')
print(' ')
sleep(1)

print('Você se depara com uma fila pequena e decide esperar sua vez.')          #Fila
sleep(2)

print(' ')
print(' ')
print('Segurança: Próximo!')
print('Faltam 4 na sua frente')
sleep(2)

print(' ')

print('Segurança: Próximo!')
print('Faltam 3 na sua frente')
sleep(2)

print(' ')

print('Segurança: Próximo!')
print('Faltam 2 na sua frente')
sleep(2)

print(' ')

print('Segurança: Próximo!')
print('Faltam 1 na sua frente')
sleep(2)

print(' ')

print('Segurança: Próximo!')
print('Agora é você!')
print(' ')
sleep(2)

                                            #Sua vez na fila

nome = input('Segurança: Qual o seu nome? ')
sleep(1)
idade = input(f'Seguraça: Qual sua idade {nome}?: ')

if int(idade) >= 18:
    print(f'Tudo bem {nome} pode entrar.')              #Aceito(a)
    sleep(1)

    print('Entrando.')
    sleep(1)
    print('Entrando..')
    sleep(1)
    print('Entrando...')
    sleep(2)

    print('Você entra e vê várias pessoas dançando, e comendo/bebendo algo')
    print(' ')

    atvd = 0
    while atvd != 4:                        #Menu de interação
        print(' ')
        print(' ')
        print('[1] Ir dançar')
        print(' ')

        print('[2] Ir ao balcão pedir algo para Comer/Beber')
        print(' ')

        print('[3] Ir tentar puxar papo com alguém')
        print(' ')

        print('[4] Sair e voltar pra casa')
        print(' ')
        print(' ')

        atvd = input('O que você vai fazer? ')                      #Ações
        if int(atvd) == 1:
            sleep(1)
            print(' ')
            print('Você decide ir dançar')
            print(' ')
            print(' ')
            sleep(3)
            print('A DJ Beatrix não consegue escolher uma música e pede para você escolher um tipo de música')                        #Easter Egg pra beatriz
            print(' ')
            print(' ')
            sleep(4)
            print('[1]-Eletrônica')
            print(' ')
            sleep(1)
            print('[2]-Româtica')
            print(' ')
            sleep(1)
            print('[3]-Hip-Hop')                                                        #Escolha de música na dança
            print(' ')
            sleep(1)
            print('[4]-Rock')
            print(' ')
            sleep(1)
            print('[5]-Funk')
            print(' ')
            print(' ')
            sleep(1)

            msc = input('Qual tipo de música você quer que ela toque? ')
            if int(msc) == 1:
                print(' ')
                print(' ')
                sleep(2)
                print('Ela agradece e começa a tocar Eletrônica')                   #Música tocando uhuul
            elif int(msc) == 2:
                print(' ')
                print('Ela agradece e começa a tocar Româtica')
            elif int(msc) == 3:
                print(' ')
                print('Ela agradece e começa a tocar Hip-Hop')
            elif int(msc) == 4:
                print(' ')
                print('Ela agradece e começa a tocar Rock')
            elif int(msc) == 5:
                print(' ')
                print('Ela agradece e começa a tocar Funk')
            print(' ')
            print(' ')
            sleep(2)
            print('Tocando a música você começa a dançar')
            print(' ')
            sleep(4)
            print('A música acaba e você volta para o centro do local')
            print(' ')
            print(' ')
                                                #Fim da Ação de Dançar
        elif int(atvd) == 2:                                                #Balcão/Comer
            sleep(1)
            print(' ')
            print(' ')
            print('Você decide ir ao balcão pedir algo para comer/beber')
            sleep(3)
            print('Chegando lá, Myrella te atende')                         #Easter Egg pra Mirella
            print(' ')
            sleep(1)
            print('Ela te apresenta a lista de Comidas e Bebidas')
            print(' ')
            print(' ')
            sleep(1)
            print('[1]-Hambúrguer')
            print(' ')
            sleep(1)

            print('[2]-Salgado')
            print(' ')                                      #Escolha de comida
            sleep(1)
            
            print('[3]-Pastel')
            print(' ')
            sleep(1)
            print(' ')
            
            cmd = input('O que vai comer? ')
            if int(cmd) == 1:
                print('Você escolheu um Hambúrguer!')
            
            elif int(cmd) == 2:
                print('Você escolheu um Salgado!')
            
            elif int(cmd) == 3:
                print('Você escolheu um Pastel!')
            
            print(' ')
            print('Agora as bebidas!')                              #Escolher Bebidas
            print(' ')
            sleep(1)

            print('[1]-Coca-Cola')
            print(' ')
            sleep(1)

            print('[2]-Mantiqueira')
            print(' ')
            sleep(1)
            
            print('[3]-Cerveja')
            print(' ')
            sleep(1)

            bbd = input('O que vai beber? ')
            if int(bbd) == 1:
                print('Você escolheu uma Coca-Cola')
            
            elif int(bbd) == 2:
                print('Você escolheu um Mantiqueira')
            
            elif int(bbd) == 3:
                print('Você escolheu uma Cerveja')
            
            print('Você se senta para comer')
            print(' ')
            sleep(4)
            print('Você termina de comer e volta ao centro do local')
            print(' ')
            print(' ')

                                                                #Fim da ação do Balcão
        
        elif int(atvd) == 3:                                    #Interção
            print('Você vai em direção a uma galera e puxa um papo')
            print(' ')
            sleep(2)
            print('Marcos: Eai cara beleza? Tá curtindo a balada?')
            print(' ')

            print('[1]-Claro mano, nunca me divertir tanto!')
            print(' ')

            print('[2]-Não muito, não conheço ninguém aqui')
            rpt = input('Digite aqui: ')
            print(' ')

            if int(rpt) == 1:
                print('Marcos: Eu também mano, chega aqui vou te apresentar uns amigos meus')
                print(' ')
                sleep(2)

                print('Marcos: Esse é o Bruno, esse aqui gosta de basquete pra caramba')
                print(' ')
                sleep(2)

                print('Bruno: Eai cara!')
                print(' ')
                sleep(2)

                print('Marcos: Essa daqui é a Anna Júlia, é a única que empata comigo no UNO!')
                print(' ')
                sleep(2)

                print('Anna: Opa turu bom?, depois vamos jogar um UNO só falar o dia')
                print(' ')
                sleep(2)
            
            elif int(rpt) ==2:
                print('Marcos: Putzzz chega aqui então mano, vou te apresentar uns amigos meus')
                print(' ')
                sleep(2)

                print('Marcos: Esse é o Bruno, esse aqui gosta de basquete pra caramba')
                print(' ')
                sleep(2)

                print('Bruno: Eai cara!')
                print(' ')
                sleep(2)

                print('Marcos: Essa daqui é a Anna Júlia, é a única que empata comigo no UNO!')
                print(' ')
                sleep(2)

                print('Anna: Opa turu bom?, depois vamos jogar um UNO só falar o dia')
                print(' ')
                sleep(2)
                                                #saindo do Local
        elif int(atvd) == 4:
            print('Você sai e volta para sua casa')
            break



elif int(idade) <= 17:
    print(' ')
    print('Segurança: Você terá que se retirar, Desculpa.')            #Recusado(a)
    print(' ')
    sleep(1)
    print('Melhor ir em uma lachonete mesmo')




