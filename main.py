from funcoes import *

acao = 0

while acao != 8:
    print("Menu")
    print("1 - Cadastrar jogador")
    print("2 - Mostrar jogadores cadastrado")
    print("3 - Mostrar relatorio completo")
    print("4 - Pesquisar jogador pelo nome")
    print("5 - Alterar informações de um jogador")
    print("6 - Remover jogador do cadastro")
    print("7 - Mostrar estatísticas gerais")
    print("8 - Encerrar programa")

    acao=int(input("Escolha a sua ação: "))

    if acao == 1:
        cadastra_jogador()
    elif acao == 2:
        mostrar_jogadores()
    elif acao == 3:
        mostrar_relatorio()
    elif acao == 4:
        pesquisar_jogador()
    elif acao == 5:
        alterar_jogador()
    elif acao == 6:
        remover_jogador()
    elif acao == 7:
        mostrar_estatisticas()
    elif acao == 8:
        print("Fechando o programa...")
        break
    else:
        print("Opção invalida, tente novamente")
        