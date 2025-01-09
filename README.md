<h2>Tecnologias e Ferramentas</h2>h2>

* Python
* JSON

<h2>Como Rodar a Aplicação</h2>

* 1) Clone o repositório para sua máquina local

* 2) Navegue até o diretório do projeto

* 3) Execute a aplicação

------------------------------------------------------------------------------

<h2>Gerenciamento de Produtos para a Loja AgilStore</h2>

* Descrição
  A AgilStore é uma pequena loja de eletrônicos que expandiu seu catálogo de produtos. Com o aumento da diversidade de itens, surgiu a necessidade de otimizar o controle de inventário, anteriormente feito de forma manual e propensa a erros. Este sistema de gerenciamento de inventário foi desenvolvido para automatizar e simplificar as operações relacionadas ao inventário, como adicionar, listar, atualizar e remover produtos.

* Funcionalidades
* 1. Adicionar Produto
Permite ao usuário adicionar um novo produto ao inventário:

Nome do Produto

Categoria

Quantidade em Estoque

Preço

Gera um ID único automaticamente para cada produto.

* 2. Listar Produtos
Exibe todos os produtos cadastrados no inventário em formato de tabela:

ID

Nome do Produto

Categoria

Quantidade em Estoque

Preço

Permite opções de filtragem por categoria ou ordenação por nome, quantidade ou preço (opcional).

* 3. Atualizar Produto
Atualiza as informações de um produto existente identificado pelo seu ID:

Verifica se o ID informado existe no inventário.

Permite atualizar Nome, Categoria, Quantidade e Preço.

Valida os novos dados antes de salvar as alterações.

* 4. Excluir Produto
Remove um produto do inventário pelo seu ID:

Verifica se o ID informado existe no inventário.

Confirma a ação com o usuário antes de excluir (opcional).

Remove o produto do inventário após a confirmação.

* 5. Buscar Produto
Busca e exibe detalhes de um produto específico pelo ID ou pelo nome:

Permite a busca por ID ou por parte do nome do produto.

Exibe todas as informações detalhadas do produto encontrado.

Exibe mensagem apropriada se nenhum produto for encontrado.
