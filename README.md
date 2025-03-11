# Documentação do Sistema de Gerenciamento de Supermercado
## 1. Introdução
Este sistema foi desenvolvido em Python para gerenciar o registro e histórico de compras de produtos em um supermercado. Ele permite que os usuários registrem compras, consultem históricos, limpem registros e gerenciem estoques de forma organizada.

O sistema segue a estrutura de Pilha (LIFO - Last In, First Out) para armazenar as compras de cada produto, garantindo que a última compra realizada seja a primeira a ser consultada.
## 2. Estrutura do Código
O código está dividido nas seguintes classes e funções:
### 2.1 Classe Compra
Representa uma compra de um produto.

#### Atributos:

• data: Data da compra (formato “AAAA-MM-DD”).

• produto: Nome do produto comprado.

• valor_compra: Preço de compra do produto.

• valor_venda: Preço de venda do produto.

• quantidade_comprada: Quantidade adquirida na compra.

• quantidade_estoque: Quantidade total disponível após a compra.

#### Métodos:

• __str__(): Retorna uma representação textual dos detalhes da compra.

### 2.2 Classe PilhaDeCompras
Gerencia a pilha de compras para um produto específico.

#### Atributos:

• compras: Lista contendo todas as compras registradas do produto.

#### Métodos:

• adicionar_compra(compra): Adiciona uma nova compra à pilha.

• obter_ultima_compra(): Retorna a última compra registrada (mais recente).

• limpar_registros(): Remove todas as compras registradas da pilha.

• listar_compras_lifo(): Retorna as compras na ordem LIFO.

### 2.3 Classe Supermercado

Gerencia o controle de compras de diferentes produtos.

#### Atributos:

• produtos: Dicionário onde as chaves são os nomes dos produtos e os valores são instâncias de PilhaDeCompras.
Métodos:

• validar_data(data_str): Verifica se a data informada está no formato correto e dentro de um intervalo aceitável.

• registrar_compra(data, produto, valor_compra, valor_venda, quantidade_comprada): Registra uma nova compra para um produto.

• consultar_historico_compras(produto): Exibe o histórico de compras de um produto específico (ordem LIFO).

• consultar_historico_completo(): Exibe o histórico completo de compras de todos os produtos.

• limpar_registro_produto(produto): Remove todas as compras registradas para um determinado produto.

• limpar_todos_registros(): Remove todas as compras registradas no sistema.

### 2.4 Funções auxiliares

#### exibir_menu()

Exibe as opções disponíveis para o usuário no menu do sistema.

#### main()

Função principal que executa o sistema, gerencia a interação do usuário e processa as opções selecionadas no menu.

## 3. Funcionamento do Sistema

### 3.1 Execução do Programa

O programa inicia com a chamada da função main(), que exibe um menu com as seguintes opções:

1. Registrar nova compra
   
• Solicita a data da compra, nome do produto, valor de compra, valor de venda e quantidade adquirida.

• Valida a data e registra a compra no sistema.

4. Consultar histórico de compras de um produto
   
• Solicita o nome do produto e exibe as compras registradas na ordem LIFO.

7. Consultar histórico completo de compras
   
• Exibe todas as compras registradas no sistema.

10. Limpar registro de um produto
    
• Remove todas as compras de um produto específico.

13. Limpar todos os registros
    
• Remove todas as compras registradas no sistema.
15. Sair

• Finaliza o programa.

### 3.2 Fluxo de Operações

1. O usuário escolhe uma opção no menu.
   
3. O sistema solicita os dados necessários (se aplicável).
   
5. A operação é executada e um feedback é exibido ao usuário.
   
7. O menu é mostrado novamente até que o usuário escolha sair.
   
4. Regras e Restrições
   
• O sistema utiliza Pilha (LIFO) para armazenar as compras de cada produto.
• A data deve ser válida e seguir o formato AAAA-MM-DD.
• O valor de compra, valor de venda e quantidade comprada devem ser números positivos.
• O estoque é atualizado conforme novas compras são registradas.
• O ano da compra não pode ser superior a 2025.

6. Exemplo de Uso
   
Registro de uma nova compra:

#### Entrada:

Digite a data da compra (formato AAAA-MM-DD): 2024-03-11  

Digite o nome do produto: Arroz  

Digite o valor de compra do produto: 5.50  

Digite o valor de venda do produto: 7.00  

Digite a quantidade comprada: 100  

#### Saída:

Compra registrada com sucesso:  

Data: 2024-03-11  

Produto: Arroz  

Valor de Compra: R$5.50  

Valor de Venda: R$7.00  

Quantidade Comprada: 100  

Quantidade em Estoque: 100  

Consulta do histórico de um produto:

#### Entrada:

Digite o nome do produto para consultar o histórico: Arroz  

#### Saída:

Histórico de compras para 'Arroz' (ordem LIFO):  

Data: 2024-03-11  

Produto: Arroz  

Valor de Compra: R$5.50  

Valor de Venda: R$7.00  

Quantidade Comprada: 100  

Quantidade em Estoque: 100  

Limpar o registro de um produto:

#### Entrada:

Digite o nome do produto para limpar o registro: Arroz  

#### Saída:

Registros de compras foram limpos.  

## 6. Conclusão

Este sistema oferece um gerenciamento simples e eficiente de compras para um supermercado, utilizando o conceito de Pilha (LIFO) para organização do histórico de compras. Ele permite registrar novas compras, consultar registros anteriores e limpar dados de forma controlada.

Este código pode ser facilmente expandido para incluir novas funcionalidades, como exportação de dados, geração de relatórios e integração com um banco de dados.

