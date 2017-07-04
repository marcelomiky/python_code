# n = número de peças dispostas
# m = número máximo de peças a ser retiradas por jogador

def computador_escolhe_jogada(n, m):
    
    # cálculos para a melhor jogada
    if (m + 1) % n == 0:
        print("Computador permite que usuário jogue agora.\n")
        proxima_jogada = 0
    else:
        print("Computador retira %d peças." % n)
        print("Há %d peças restantes.\n" % (m - n))
        proxima_jogada = n
    return proxima_jogada

def usuario_escolhe_jogada(n, m):
    
    jogada_usuario = int(input("Informe sua jogada: "))
                         
    while jogada_usuario <= 0 or jogada_usuario > n:
        print("Valor incorreto. O valor deve estar entre 1 e", n)
        jogada_usuario = int(input("Informe sua jogada: "))
    
    print("Usuário retira %d peças." % jogada_usuario)
    print("Há %d peças restantes.\n" % (m - jogada_usuario))
    return jogada_usuario

def partida():
    m = int(input("Informe o valor das peças dispostas:"))
    n = int(input("Informe o valor de máximo de peças a ser retiradas:"))
    
    vencedor = 2 # variável de controle para quem venceu. 1 para cpu, 0 para usuário.
    
    peças_restantes = m
            
    while peças_restantes > 0:
        
        # jogada computador
        peças_retiradas = computador_escolhe_jogada(n, peças_restantes)
        peças_restantes = peças_restantes - peças_retiradas

        if peças_restantes == 0:
            vencedor = 1
            break
            
        # jogada usuaŕio
        peças_retiradas = usuario_escolhe_jogada(n, peças_restantes)
        peças_restantes = peças_restantes - peças_retiradas

        if peças_restantes == 0:
            vencedor = 0
            break
    
    if vencedor == 1:
        print("Fim de jogo! O computador ganhou!\n")
        return 1
    elif vencedor == 0:
        print("Fim de jogo! Você ganhou!\n")
        return 0

def campeonato():
    
    rodada = 1
    
    partidas_ganhas_cpu = 0
    partidas_ganhas_usuario = 0
    
    while rodada <= 3:
        print("**** Rodada %d ****" % rodada)
        vencedor = partida()
        if vencedor == 1:
            partidas_ganhas_cpu += 1
        elif vencedor == 0:
            partidas_ganhas_usuario += 1
        rodada += 1
    
    print("**** Final do campeonato! ****\n")
    print("Placar: Você %d x %d Computador" % (partidas_ganhas_usuario, partidas_ganhas_cpu))

def main():
    
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    
    escolha = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n"))
    
    if escolha == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    elif escolha == 2:
        print("Você escolheu um campeonato!")
        campeonato()

if __name__ == "__main__":
    main()

