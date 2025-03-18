# Documentação do Sistema de Controle de Compras e Estoque para Supermercado

## 1. Introdução

Este sistema gerencia as compras e vendas de produtos em um supermercado, utilizando uma estrutura de pilha (LIFO - Último a Entrar, Primeiro a Sair) para armazenar as compras. Ele permite registrar compras, realizar vendas, consultar histórico de compras e estoque, além de limpar registros de produtos.

## 2. Estrutura do Código

O sistema é organizado em três classes principais:

- **Compra**: Representa uma compra de um produto.
- **PilhaDeCompras**: Gerencia a pilha de compras de um produto.
- **Supermercado**: Administra os produtos, compras, vendas e consultas.

Há também um menu interativo para interação do usuário.

## 3. Classes e Métodos

### 3.1 Classe Compra

Representa uma compra realizada no supermercado.

#### Atributos

- **data**: Data da compra.
- **produto**: Nome do produto.
- **valor_compra**: Preço pago por unidade.
- **valor_venda**: Preço de venda (atualmente igual ao preço de compra).
- **quantidade_comprada**: Quantidade adquirida.
- **quantidade_estoque**: Estoque após a compra.

### 3.2 Classe PilhaDeCompras

Gerencia a pilha de compras de um produto.

#### Atributo

- **compras**: Lista de objetos `Compra` representando o histórico de compras.

#### Métodos

- **adicionar_compra**: Adiciona uma compra à pilha.
- **obter_ultima_compra**: Retorna a última compra realizada.
- **limpar_registros**: Remove todas as compras do produto.
- **listar_compras_lifo**: Retorna as compras em ordem LIFO.

### 3.3 Classe Supermercado

Gerencia compras, vendas e estoque.

#### Atributo

- **produtos**: Dicionário onde a chave é o nome do produto e o valor é um objeto `PilhaDeCompras`.

#### Métodos

- **validar_data**: Verifica se a data está no formato correto (AAAA-MM-DD) e dentro do ano permitido.
- **registrar_compra**: Registra uma nova compra e atualiza o estoque.
- **realizar_venda**: Processa a venda e reduz a quantidade em estoque.
- **consultar_historico_compras**: Exibe o histórico de compras de um produto.
- **consultar_historico_completo**: Exibe o histórico de todos os produtos.
- **consultar_estoque**: Exibe a quantidade em estoque.
- **limpar_registro_produto**: Apaga o histórico de um produto.
- **limpar_todos_registros**: Remove todos os registros de compras.

## 4. Interface do Usuário (Menu)

O sistema apresenta um menu interativo com as seguintes opções:

1. Registrar nova compra  
2. Consultar histórico de compras de um produto  
3. Consultar histórico completo de compras  
4. Consultar estoque de produtos  
5. Realizar venda de um produto  
6. Limpar registro de um produto  
7. Limpar todos os registros  
8. Sair  

O menu roda em um loop até que o usuário escolha a opção "Sair".

## 5. Funcionamento do Sistema

1. O programa inicia criando um objeto `Supermercado`.
2. O usuário interage com o menu e escolhe uma opção.
3. Dependendo da escolha, o sistema executa a operação correspondente.
4. As informações são armazenadas em pilhas para cada produto.
5. O usuário pode encerrar o programa a qualquer momento.

## 6. Regras e Validações

- **Formato de Data**: Deve ser AAAA-MM-DD e o ano não pode ser superior a 2025.
- **Controle de Estoque**: Impede a venda de mais unidades do que o disponível.
- **Ordem LIFO**: As consultas de compras mostram primeiro as mais recentes.

## 7. Conclusão

Este sistema fornece um gerenciamento eficiente para supermercados, garantindo um controle organizado das compras e vendas. Ele é simples, funcional e pode ser expandido conforme necessário.
