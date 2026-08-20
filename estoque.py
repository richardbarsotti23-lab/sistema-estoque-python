"""
Sistema de Controle de Estoque
Autor: Richard Barsotti Silva

Sistema simples via terminal para gerenciar produtos em estoque:
cadastro, listagem, atualização de quantidade, edição e remoção.
"""

estoque = {}
proximo_id = 1


def exibir_menu():
    """Exibe o menu principal do sistema."""
    print("\n===== SISTEMA DE ESTOQUE =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar quantidade")
    print("4 - Editar produto")
    print("5 - Remover produto")
    print("6 - Buscar produto")
    print("7 - Sair")


def obter_numero(mensagem, tipo=float):
    """Solicita um número ao usuário, validando a entrada."""
    while True:
        try:
            return tipo(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def cadastrar_produto():
    """Cadastra um novo produto no estoque."""
    global proximo_id
    nome = input("Nome do produto: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        return

    quantidade = int(obter_numero("Quantidade inicial: ", int))
    preco = obter_numero("Preço unitário (R$): ", float)

    estoque[proximo_id] = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }
    print(f"Produto '{nome}' cadastrado com ID {proximo_id}.")
    proximo_id += 1


def listar_produtos():
    """Lista todos os produtos cadastrados no estoque."""
    if not estoque:
        print("Nenhum produto cadastrado.")
        return

    print(f"\n{'ID':<5}{'Nome':<20}{'Qtd':<10}{'Preço (R$)':<12}")
    print("-" * 47)
    for produto_id, dados in estoque.items():
        print(f"{produto_id:<5}{dados['nome']:<20}{dados['quantidade']:<10}{dados['preco']:<12.2f}")


def buscar_produto():
    """Busca um produto pelo ID e exibe seus dados."""
    produto_id = int(obter_numero("ID do produto: ", int))
    produto = estoque.get(produto_id)
    if produto:
        print(f"\nID: {produto_id}")
        print(f"Nome: {produto['nome']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
    else:
        print("Produto não encontrado.")


def atualizar_quantidade():
    """Adiciona ou remove unidades da quantidade de um produto."""
    produto_id = int(obter_numero("ID do produto: ", int))
    if produto_id not in estoque:
        print("Produto não encontrado.")
        return

    print("1 - Adicionar unidades")
    print("2 - Remover unidades")
    opcao = input("Escolha: ")

    quantidade = int(obter_numero("Quantidade: ", int))

    if opcao == "1":
        estoque[produto_id]["quantidade"] += quantidade
        print("Quantidade atualizada com sucesso.")
    elif opcao == "2":
        if quantidade > estoque[produto_id]["quantidade"]:
            print("Erro: quantidade insuficiente em estoque.")
        else:
            estoque[produto_id]["quantidade"] -= quantidade
            print("Quantidade atualizada com sucesso.")
    else:
        print("Opção inválida.")


def editar_produto():
    """Edita nome e/ou preço de um produto existente."""
    produto_id = int(obter_numero("ID do produto: ", int))
    if produto_id not in estoque:
        print("Produto não encontrado.")
        return

    novo_nome = input(f"Novo nome (atual: {estoque[produto_id]['nome']}, Enter para manter): ").strip()
    if novo_nome:
        estoque[produto_id]["nome"] = novo_nome

    novo_preco = input(f"Novo preço (atual: {estoque[produto_id]['preco']:.2f}, Enter para manter): ").strip()
    if novo_preco:
        try:
            estoque[produto_id]["preco"] = float(novo_preco)
        except ValueError:
            print("Preço inválido, mantendo o valor anterior.")

    print("Produto atualizado com sucesso.")


def remover_produto():
    """Remove um produto do estoque."""
    produto_id = int(obter_numero("ID do produto: ", int))
    if produto_id in estoque:
        nome = estoque[produto_id]["nome"]
        del estoque[produto_id]
        print(f"Produto '{nome}' removido com sucesso.")
    else:
        print("Produto não encontrado.")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            atualizar_quantidade()
        elif opcao == "4":
            editar_produto()
        elif opcao == "5":
            remover_produto()
        elif opcao == "6":
            buscar_produto()
        elif opcao == "7":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
