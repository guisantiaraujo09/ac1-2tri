from listas import nomeJogadores, quantPartidas, quantGols

def cadastra_jogador():

    continuar="s"
    while continuar == "s":
            nome=input("digite o nome do jogador: ")
            partidas=int(input("digite a quantidade de partidas: "))
            gols=int(input("digite a quantidade de gols: "))

            nomeJogadores.append(nome)
            quantPartidas.append(partidas)
            quantGols.append(gols)

            print("Jogador cadastrado com sucesso")

            continuar =input("Deseja cadastrar outro aluno? (s/n): ")

def mostrar_jogadores():
    if len(nomeJogadores)==0:
        print("Não possui jogadores cadastrados")
    else:
        for i in range(len(nomeJogadores)):
            print(f"Nome jogador: {nomeJogadores[i]}")  
            print(f"Quantidade de partidas: {quantPartidas[i]}")      
            print(f"Quantidade de gols: {quantGols[i]}")


def mostrar_relatorio():
    if len(nomeJogadores)==0:
        print("Nao possui jogadores cadastrados")
    else:
        for i in range(len(nomeJogadores)):
            gols=quantGols[i]
            partidas=quantPartidas[i]
            media=gols/partidas

            if media<=1:
                print(f"Nome jogador: {nomeJogadores[i]}, quantidade de partidas {quantPartidas[i]} e de gols {quantGols[i]}")
                print(f"Voce precisa melhorar, sua media e de: {media}")
            elif media<2:
                print(f"Nome jogador: {nomeJogadores[i]}, quantidade de partidas {quantPartidas[i]} e de gols {quantGols[i]}")
                print(f"Voce foi bem, sua media e de: {media}")
            else:
                print(f"Nome jogador: {nomeJogadores[i]}, quantidade de partidas {quantPartidas[i]} e de gols {quantGols[i]}")
                print(f"Voce foi excelente, sua media e de: {media}")



def pesquisar_jogador():
    if len(nomeJogadores)==0:
        print("Nao possui jogadores cadastrados")
    else:
        pesquisar=input("Digite o nome do jogador: ")
        if pesquisar in nomeJogadores:
            posicao=nomeJogadores.index(pesquisar)
            print("Jogador encontrado: ")
            print(nomeJogadores[posicao])
        else:
            print("Jogador nao encontrado ou digitou o nome errado")

def alterar_jogador():
    acao=0
    while acao !=3:
        print("1 - Alterar dados do jogador")
        print("2 - Excluir jogador")
        print("3 - Encerrar alterações")

        acao=int(input("Qual ação deseja fazer: "))
        if acao==1:
            if len(nomeJogadores)==0:
                print("Nao possui jogadores cadastrados")
            else:
                jogador=input("Digite o nome do jogador: ")
                if jogador in nomeJogadores:
                    posicao=nomeJogadores.index(jogador)
                    novoJogador=input("Digite o novo nome do jogador: ")
                    nomeJogadores[posicao]=novoJogador
                    print("Nome do jogador trocado com sucesso")
                else:
                    print("Jogador nao encontrado ou digitou o nome errado")
        elif acao == 2:
            if len(nomeJogadores) == 0:
                print("Não possui jogadores cadastrados")
            else:
                jogador = input("Digite o nome do jogador que deseja excluir: ")
                if jogador in nomeJogadores:
                    posicao = nomeJogadores.index(jogador)
                    nomeJogadores.pop(posicao)
                    quantPartidas.pop(posicao)
                    quantGols.pop(posicao)
                    print("Jogador removido com sucesso!")
                else:
                    print("Jogador não encontrado.")
        else:
            print("Encerrando alterações")
            break

def remover_jogador():
    if len(nomeJogadores) == 0:
        print("Não possui jogadores cadastrados.")
    else:
        jogador = input("Digite o nome do jogador que deseja remover: ")
        if jogador in nomeJogadores:
            posicao =nomeJogadores.index(jogador)
            nomeJogadores.pop(posicao)
            quantPartidas.pop(posicao)
            quantGols.pop(posicao)
            print("Jogador removido com sucesso!")
        else:
            print("Jogador não encontrado.")

def mostrar_estatisticas():
    if len(nomeJogadores) == 0:
        print("Nenhum jogador cadastrado.")
    else:
        medias = []
        excelentes = 0
        melhorar = 0
        for i in range(len(nomeJogadores)):
            if quantPartidas[i]>0:
                media =quantGols[i]/quantPartidas[i]
            else:
                media=0   
            medias.append(media)
            if media >= 2:
                excelentes += 1
            elif media < 1:
                melhorar += 1
            
    print(f"1-Quantidade de jogadores: {len(nomeJogadores)}")
    print(f"2-Melhor media: {max(medias)}")
    print(f"3-Menor media: {min(medias)}")
    print(f"4-Média geral dos jogadores: {sum(medias)/len(medias)}")
    print(f"5-Jogador com melhor desempenho: {nomeJogadores[medias.index(max(medias))]}")
    print(f"6-Jogadores com excelente: {excelentes}")
    print(f"7-Jogadores que precisam melhorar: {melhorar}")




