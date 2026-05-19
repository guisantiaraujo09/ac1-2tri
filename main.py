from funcoes import cadastra_jogador, mostrar_jogadores

acao = 0

while acao != 9:

    print("\nMENU")
    print("1 - Cadastrar jogador")
    print("2 - Mostrar jogadores cadastrado")
    print("3 - Mostrar relatorio completo")
    print("4 - Pesquisar jogador pelo nome")
    print("5 - Alterar informações de um jogador")
    print("6 - Remover jogador do cadastro")
    print("7 - Mostrar estatísticas gerais")
    print("8 - Encerrar programa")
    print("9 - Sair")

    acao=int(input("Escolha a sua ação: "))

    if acao == 1:
        cadastra_jogador()
    elif acao == 2:
        mostrar_jogadores()

        