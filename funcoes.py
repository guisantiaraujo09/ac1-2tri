from listas import nomeJogadores, quantPartidas, quantGols


def cadastra_jogador():

    continuar="s"
    while continuar == "s":
            nome=input("digite o nome do jogador: ")
            partidas=input("digite a quantidade de partidas: ")
            gols=input("digite a quantidade de gols: ")

            nomeJogadores.append(nome)
            quantPartidas.append(partidas)
            quantGols.append(gols)

            print("Jogador cadastrado com sucesso")

            continuar =input("Deseja cadastrar outro aluno? (s/n): ")

def mostrar_jogadores():
      print(f"Jogadores cadastrados: {nomeJogadores}")
            



