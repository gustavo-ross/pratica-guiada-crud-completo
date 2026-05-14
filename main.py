import os
import banco
import funcoes_cliente as fc

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\n Precione ENTER para continuar...")


def iniciar_sistema():
    banco.criar_tabela()

    while True:
        limpar_tela()
        print("=" * 10)
        print("    SISTEMA DE GESTÃO 1.0    ")
        print("=" * 10)
        print("[1] Novo Cliente")
        print("[2] Listar Clientes")
        print("[3] Atualizar E-mail")
        print("[4] Excluir Cliente")
        print("[0] Sair do Sistema")

        opcao = input("\n➡️ Escolha uma opção: ")

        limpar_tela()

        match opcao:
            case "1":
                fc.cadastrar_cliente()
            case "2":
                fc.listar_clientes()
            case "3":
                fc.atualizar_email()
            case "4":
                fc.excluir_cliente()
            case"0":
                print("Desligando o sistema... Até logo!")
                break
            case _:
                print("❌ Opção inválida. Tente novamente.")

        if opcao != 0:
            pausar()


if __name__ == "__main__":
    iniciar_sistema()