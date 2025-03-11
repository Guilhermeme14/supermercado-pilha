class Compra:
    def __init__(self, data, produto, valor_compra, valor_venda, quantidade_comprada, quantidade_estoque):
        self.data = data
        self.produto = produto
        self.valor_compra = valor_compra
        self.valor_venda = valor_venda
        self.quantidade_comprada = quantidade_comprada
        self.quantidade_estoque = quantidade_estoque

    def __str__(self):
        return (f"Data: {self.data}\n"
                f"Produto: {self.produto}\n"
                f"Valor de Compra: R${self.valor_compra:.2f}\n"
                f"Valor de Venda: R${self.valor_venda:.2f}\n"
                f"Quantidade Comprada: {self.quantidade_comprada}\n"
                f"Quantidade em Estoque: {self.quantidade_estoque}")

class PilhaDeCompras:
    def __init__(self):
        self.compras = []

    def adicionar_compra(self, compra):
        self.compras.append(compra)  # Adiciona no final da lista (topo da pilha)

    def obter_ultima_compra(self):
        if self.compras:
            return self.compras[-1]  # Retorna o último elemento (topo da pilha)
        return None

    def limpar_registros(self):
        self.compras.clear()
        print(f"Registros de compras foram limpos.")

    def listar_compras_lifo(self):
        # Retorna as compras em ordem LIFO (do último ao primeiro)
        return reversed(self.compras)

class Supermercado:
    def __init__(self):
        self.produtos = {}

    def registrar_compra(self, data, produto, valor_compra, valor_venda, quantidade_comprada):
        if produto not in self.produtos:
            self.produtos[produto] = PilhaDeCompras()

        pilha_de_compras = self.produtos[produto]
        ultima_compra = pilha_de_compras.obter_ultima_compra()

        # Define a quantidade em estoque
        quantidade_estoque = quantidade_comprada if not ultima_compra else ultima_compra.quantidade_estoque + quantidade_comprada

        # Cria uma nova compra
        nova_compra = Compra(data, produto, valor_compra, valor_venda, quantidade_comprada, quantidade_estoque)
        pilha_de_compras.adicionar_compra(nova_compra)
        print(f"Compra registrada com sucesso: \n{nova_compra}")

    def consultar_historico_compras(self, produto):
        if produto in self.produtos:
            pilha_de_compras = self.produtos[produto]
            if pilha_de_compras.compras:
                print(f"Histórico de compras para '{produto}' (ordem LIFO):")
                for compra in pilha_de_compras.listar_compras_lifo():  # Exibe em ordem LIFO
                    print(compra)
            else:
                print(f"Nenhuma compra registrada para o produto '{produto}'.")
        else:
            print(f"Produto '{produto}' não encontrado.")

    def consultar_historico_completo(self):
        if not self.produtos:
            print("Nenhum produto registrado no sistema.")
            return

        print("\n--- Histórico Completo de Compras (ordem LIFO) ---")
        for produto, pilha_de_compras in self.produtos.items():
            print(f"\nProduto: {produto}")
            if pilha_de_compras.compras:
                for compra in pilha_de_compras.listar_compras_lifo():  # Exibe em ordem LIFO
                    print(compra)
            else:
                print("Nenhuma compra registrada para este produto.")

    def limpar_registro_produto(self, produto):
        if produto in self.produtos:
            self.produtos[produto].limpar_registros()
        else:
            print(f"Produto '{produto}' não encontrado.")

    def limpar_todos_registros(self):
        self.produtos.clear()
        print("Todos os registros de compras foram limpos.")

# Função para exibir o menu
def exibir_menu():
    print("\n--- Menu do Supermercado ---")
    print("1. Registrar nova compra")
    print("2. Consultar histórico de compras de um produto")
    print("3. Consultar histórico completo de compras")
    print("4. Limpar registro de um produto")
    print("5. Limpar todos os registros")
    print("6. Sair")

# Programa principal
def main():
    supermercado = Supermercado()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            data = input("Digite a data da compra (ex: 2023-10-01): ")
            produto = input("Digite o nome do produto: ")
            valor_compra = float(input("Digite o valor de compra do produto: "))
            valor_venda = float(input("Digite o valor de venda do produto: "))
            quantidade_comprada = int(input("Digite a quantidade comprada: "))
            supermercado.registrar_compra(data, produto, valor_compra, valor_venda, quantidade_comprada)

        elif opcao == "2":
            produto = input("Digite o nome do produto para consultar o histórico: ")
            supermercado.consultar_historico_compras(produto)

        elif opcao == "3":
            supermercado.consultar_historico_completo()

        elif opcao == "4":
            produto = input("Digite o nome do produto para limpar o registro: ")
            supermercado.limpar_registro_produto(produto)

        elif opcao == "5":
            confirmacao = input("Tem certeza que deseja limpar todos os registros? (s/n): ")
            if confirmacao.lower() == "s":
                supermercado.limpar_todos_registros()

        elif opcao == "6":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    main()