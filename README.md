# Exercício: Desenvolvimento Guiado por Testes (TDD) na E-MagicShop

## Contexto:

Dentro de uma startup inovadora chamada "E-MagicShop", você faz parte de uma equipe que está no processo de construir uma plataforma de loja eletrônica revolucionária. Neste exercício, você será introduzido ao conceito de Test-Driven Development (TDD). 

No TDD, o desenvolvedor começa escrevendo testes para a nova funcionalidade antes mesmo de escrever o código de produção. Sua tarefa é garantir que cada teste seja rigorosamente escrito e coberto antes da implementação da funcionalidade.

## Sua Missão:

1. **Desenvolvedor**: Comece escrevendo testes unitários para cada funcionalidade antes de implementá-la. Não precisa criar todos os testes de todas as funcionalidades antes de começar a desenvolvimento, implemente os testes de cada funcionalidade e já desenvolva a funcionalidade. Por exemplo, cadastro de usuario, crie os testes do cadastro de usuários e em seguida desenvolva a funcionalidade e assim por diante.

## Banco de Dados:

Estaremos usando o SQLite para este exercício. Serão três tabelas: Usuários, Produtos e Classificações.

## Requisitos Detalhados:

Para cada recurso listado abaixo, você deve criar as operações de CRUD (Create, Read, Update, Delete). No contexto deste exercício, "Read" se divide em dois: pesquisa de um único item e pesquisa de todos os itens.

1. **Usuários**:
   - **Cadastrar** um usuário:
     - Recebe os detalhes do usuário e adiciona ao banco de dados.
     - Validações:
       - Idade: entre 0 e 120. Se inválido, retorne `False`.
       - CPF: deve ter exatamente 11 caracteres. Se inválido, retorne `False`.
       - E-mail: deve conter "@" e ter caracteres antes e após ele. Se inválido, retorne `False`.
   - **Ler** detalhes de um único usuário:
     - Recebe o ID de um usuário e retorna seus detalhes.
   - **Ler** detalhes de todos os usuários:
     - Retorna uma lista com detalhes de todos os usuários.
   - **Atualizar** um usuário:
     - Recebe o ID e os novos detalhes de um usuário para atualizar no banco de dados.
     - As mesmas validações do cadastro devem ser aplicadas aqui.
   - **Deletar** um usuário:
     - Recebe o ID de um usuário e o remove do banco de dados.

2. **Produtos**:
   - **Cadastrar** um produto:
     - Recebe os detalhes do produto e adiciona ao banco de dados.
     - Validações:
       - Preço: não pode ser negativo. Se inválido, retorne `False`.
       - Estoque: não pode ser negativo. Se inválido, retorne `False`.
       - Categoria: deve pertencer a uma lista pré-definida de categorias. Se inválido, retorne `False`.
   - **Ler** detalhes de um único produto:
     - Recebe o ID de um produto e retorna seus detalhes.
   - **Ler** detalhes de todos os produtos:
     - Retorna uma lista com detalhes de todos os produtos.
   - **Atualizar** um produto:
     - Recebe o ID e os novos detalhes de um produto para atualizar no banco de dados.
     - As mesmas validações do cadastro devem ser aplicadas aqui.
   - **Deletar** um produto:
     - Recebe o ID de um produto e o remove do banco de dados.

3. **Classificações**:
   - **Cadastrar** uma classificação:
     - Recebe os detalhes da classificação e adiciona ao banco de dados.
     - Validação: `id_usuario` e `id_produto` devem existir nas respectivas tabelas. Se inválido, retorne `False`.
   - **Ler** detalhes de uma única classificação:
     - Recebe os IDs de um usuário e de um produto e retorna a classificação correspondente.
   - **Ler** detalhes de todas as classificações:
     - Retorna uma lista com detalhes de todas as classificações.
   - **Atualizar** uma classificação:
     - Recebe os IDs de um usuário e de um produto, juntamente com o novo comentário, e atualiza no banco de dados.
   - **Deletar** uma classificação:
     - Recebe os IDs de um usuário e de um produto e remove a classificação correspondente do banco de dados.


## Dicas e Recomendações:

- Crie um arquivo separado para manipulação do banco de dados.
- Implemente funções separadas para cada operação do CRUD de cada recurso.
- Ao criar testes, pense em todos os cenários possíveis: fluxos felizes e fluxos de falha que precisam ser tratados.
