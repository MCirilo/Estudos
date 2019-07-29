  
        
def computador_escolhe_jogada(n, m):
    
    computadorRetira = 1

    while computadorRetira != m:

        if (n - computadorRetira) % (m+1) == 0:

            return computadorRetira
        
        else:

            computadorRetira += 1
        
    return computadorRetira
    
def usuario_escolhe_jogada(n, m):
    jogadaValida = False

    while not jogadaValida:
        jogadorRetira = int(input("Quantas peças deseja tirar? "))

        if jogadorRetira > m or jogadorRetira < 1:

            print("Jogada invalida!")
                    
        else:
            jogadaValida = True
            
    return jogadorRetira

def campeonato():
    x = 1
    while x <= 3:
        
        print()
        print('partida', x)
        partida_isolada()
        print()
        x += 1

def partida_isolada():
    
    n = int(input("Escolha o numero da de peças: "))

    m = int(input("Limite de peças por jogada: "))

    computadorEscolhe = True

    if n % (m+1) == 0:
        print()
        print("O computador passou")

    else:
        print()
        print("O computador começa!")
        computadorEscolhe = True
    
    while n > 0:
        if computadorEscolhe:
            computadorRetira = computador_escolhe_jogada(n, m)
            n = n - computadorRetira
            if computadorRetira == 1:
                print()
                print("Computador tirou uma peça")
            else:
                print()
                print("Computador tirou", computadorRetira, "peças")

            computadorEscolhe = False
        else:
            jogadorRetira = usuario_escolhe_jogada(n, m)
            n = n - jogadorRetira

            if jogadorRetira == 1:
                print()
                print("Usario tirou 1 peça")
            else:
                print()
                print("Usuario tirou", jogadorRetira, "peças")

            computadorEscolhe = True

        if n == 1:
                print("So resta apenas 1 peça")
                print()
        else:

            if n !=0:
                print("Agora restam,", n, "peças no tabuleiro.")
                print()

    print('Fim do jogo! O computador ganhou!')
    
print("Bem vindo ao jogo do NIM! Escolha:")

print("1 - Para jogar uma partida isolada ")
print("2 - Para jogar um cammpeonato")

x = int(input("Escolha o modo: "))

if x == 1:
    print("Partida isoalda escolhida!")
    partida_isolada()
else:
    if x == 2:
        print("Campeonato escolhido!")
        campeonato()

    
    
    
