# Gestor de estoque

O programa auxilia em toda parte de gestão de estoque, desde a parte de cadastro até o historico de alterações e logs de usuário.

## Origem do projeto
Este projeto nasceu de um trabalho da faculdade que pedia um gerenciador de estoque. Implementei mais funcionalidades do que o solicitado e decidi continuar evoluindo o código por conta própria.


## Funcionalidades

- Cadastro de produtos, com validação de nome, data e saldo inicial.
- Entrada e saída de produtos, com atualização automática do saldo.
- Bloqueio de saída quando a quantidade pedida é maior que o saldo.
- Consulta de saldo geral ou de um item.
- Histórico de movimentações, geral ou por item, com item, tipo de ação, quantidade, responsável e data gerada pelo sistema.
- Menu com submenus e tratamento de entradas inválidas.

## Como executar

### Requisitos
- Python 3.13.7
- Nenhuma dependência externa

### Passos
1. Clone o repositório:
   ```
   git clone [ ] URL-do-repositório
   ```
2. Entre na pasta:
   ```
   cd Gestor_estoque
   ```
3. Execute:
   ```
   python Gestor_estoque.py
   ```
4. Informe seu nome de usuário e navegue pelo menu, digitando de **a** até **e**.

## Limitações atuais

- Os dados ficam só em memória: ao fechar o programa, estoque e histórico são perdidos.
- O nome do item é o identificador: variações de acento ou grafia criam itens distintos.
- Nas opções de entrada e baixa, não há como cancelar ao informar um item inexistente.
- O responsável é um nome digitado, sem autenticação.
- Na entrada e na saída, a data é gerada pelo sistema e não informada pelo usuário.
- Código com muita repetição e estrutura aninhada, a ser refatorado.



## Roadmap

- [ ] Refatorar em funções, separando interação com o usuário e regra de negócio
- [ ] Permitir cancelar operações nos fluxos de entrada e baixa
- [ ] Persistir os dados (arquivo e depois banco de dados)
- [ ] Usar identificador próprio para os itens
- [ ] Padronizar o vocabulário das movimentações
- [ ] Testes automatizados

## Diário de evolução

Cada etapa relevante será registrada aqui, com o que mudou e o que aprendi.

| Versão | O que mudou | O que aprendi |
|--------|-------------|---------------|
| v1.0 | Versão inicial, derivada da atividade da faculdade | Dicionários e listas, funções, datas com `datetime`, validação com `try/except`, laços `while` com `break` e `continue`, menus com `if/elif` e regras de negócio |