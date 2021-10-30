from time import sleep
nomes = []
emails = []
senhas = []

print(' ')
print(' ')
print('                   \033[1;34;34mGG Company \033[m')
print(' ')
print(' ')
sleep(2)
print('Bem vindo a GG Company')
print('Aqui você pode publicar seus jogos para o público jogar')
print(' ')
print('Antes faça seu Login!')
print(' ')
sleep(1)
op = 1
while op:
    print('[ 1 ] - Login')
    print('[ 2 ] - Cadastrar')
    print('[ 3 ] - Sair')
    print(' ')
    op = int(input('Escolha uma opção: '))
    if op == 1:
        sleep(2)
        print(' ')
        print('Ótimo vamos lá')
        nome = input('Aqui coloque seu nome completo: ')
        if nome in nomes:
            print(' ')
            email = input('Coloque seu email: ')
            if email in emails:
                print(' ')
                senha = input('Coloque sua senha: ')
                if senha in senhas:
                    print(' BEM VINDO!')
                    sleep(3)
                    print('Estamos em desenvolvimento')
                    sleep(1)
                    print('Então até a próxima adeus')
                    break
                else:
                    print('Senha inválida ou não está cadastrado tente denovo')
            else:
                print('Email não cadastrado')
        else:
            print('Cadastre primeiro antes de entrar')
            print(' ')

        

    elif op == 2:
        sleep(2)
        print(' ')
        print('Não tem um login pronto?')
        print(' ')
        sleep(1)
        print('Vamos fazer um então!')
        print(' ')
        sleep(1)

        nome = input('Aqui coloque seu nome completo: ')
        nomes.append(nome)
        sleep(1)

        email = input('Aqui coloque seu email: ')
        emails.append(email)

        senha = input('Aqui coloque uma senha: ')
        senhas.append(senha)
        print(' ')
        sleep(2)
        print('Agora faça login')
        print(' ')
    
    else:
        print('Obrigado por acessar, até a próxima!')
        break
