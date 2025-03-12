# Documentação do Sistema de Controle de Compras e Estoque para Supermercado

## 1. Introdução

Este sistema tem como objetivo gerenciar as compras e vendas de produtos em um supermercado, utilizando uma estrutura de pilha (LIFO) para armazenar as compras de cada produto. Ele permite registrar compras, realizar vendas, consultar histórico de compras e estoque, além de limpar registros de produtos.

## 2. Estrutura do Código

O código é organizado em três classes principais:

1. Compra: Representa uma compra de um determinado produto.

2. PilhaDeCompras: Gerencia a pilha de compras de um produto específico.

3. Supermercado: Administra os produtos, compras, vendas e consultas do sistema.

Além disso, há um menu interativo para o usuário interagir com o sistema.

## 3. Classes e Métodos

### 3.1 Classe Compra

Representa uma compra realizada no supermercado.

#### Atributos

• data (str): Data da compra.

• produto (str): Nome do produto adquirido.

• valor_compra (float): Preço pago por unidade do produto.

• valor_venda (float): Preço de venda do produto (atualmente igual ao preço de compra).

• quantidade_comprada (int): Quantidade adquirida do produto.

• quantidade_estoque (int): Quantidade disponível em estoque após a compra.

#### Métodos

• __str__(): Retorna uma string formatada com as informações da compra.


### 3.2 Classe PilhaDeCompras


Gerencia uma pilha de compras de um determinado produto (LIFO - Último a Entrar, Primeiro a Sair).


#### Atributos

• compras (list): Lista de objetos Compra, representando o histórico de compras.


#### Métodos

• adicionar_compra(compra): Adiciona uma nova compra ao topo da pilha.

• obter_ultima_compra(): Retorna a última compra realizada (topo da pilha).

• limpar_registros(): Remove todas as compras do produto.

• listar_compras_lifo(): Retorna a lista de compras em ordem LIFO (última compra primeiro).


### 3.3 Classe Supermercado


Gerencia o controle de compras, vendas e estoque.


## Atributos

• produtos (dict): Dicionário onde a chave é o nome do produto e o valor é um objeto PilhaDeCompras.


## Métodos

• validar_data(data_str): Verifica se a data inserida pelo usuário está no formato correto (AAAA-MM-DD) e dentro do ano permitido (até 2025).

• registrar_compra(data, produto, valor_compra, quantidade_comprada): Registra uma nova compra e atualiza o estoque do produto.

• realizar_venda(produto, quantidade_vendida): Processa a venda de um produto, reduzindo a quantidade em estoque.

• consultar_historico_compras(produto): Exibe o histórico de compras de um produto específico.

• consultar_historico_completo(): Exibe o histórico de compras de todos os produtos.

• consultar_estoque(): Exibe a quantidade disponível em estoque para cada produto.

• limpar_registro_produto(produto): Apaga o histórico de compras de um único produto.

• limpar_todos_registros(): Remove todos os registros de compras do sistema.


# 4. Interface do Usuário (Menu)


O sistema apresenta um menu interativo, permitindo que o usuário escolha entre diversas opções:

1. Registrar nova compra

2. Consultar histórico de compras de um produto

3. Consultar histórico completo de compras

4. Consultar estoque de produtos

5. Realizar venda de um produto

6. Limpar registro de um produto

7. Limpar todos os registros

8. Sair


O menu roda em um loop infinito até que o usuário escolha a opção “Sair”.


5. Como o Código Funciona

1. O programa inicia criando um objeto Supermercado.

2. O usuário interage com o menu e escolhe uma opção digitando um número.

3. Dependendo da escolha, o sistema executa operações como registrar compras, consultar estoque ou realizar vendas.

4. As informações são armazenadas e gerenciadas dentro de pilhas para cada produto.

5. O usuário pode encerrar o programa a qualquer momento selecionando a opção “Sair”.


# 6. Regras e Validações

• Formato de Data: Deve ser AAAA-MM-DD, e o ano não pode ser superior a 2025.

• Quantidade e Preço: O usuário deve inserir valores numéricos válidos.

• Controle de Estoque: O sistema impede a venda de mais unidades do que o disponível.

• Ordem LIFO: As consultas de compras mostram primeiro as mais recentes.


# 7. Possíveis Melhorias

• Implementar um banco de dados para persistência dos dados.

• Melhorar a interface para um sistema gráfico (GUI).

• Permitir a atualização automática do valor de venda baseado na média dos preços de compra.


# 8. Conclusão


Este sistema fornece um gerenciamento eficiente para supermercados, garantindo um controle organizado das compras e vendas. Ele é simples, funcional e pode ser expandido conforme necessário.
