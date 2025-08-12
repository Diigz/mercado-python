## Market_In_Terminal

Um sistema simples em Python para gerenciar um carrinho de compras diretamente no terminal — ideal para aprender estruturas de dados básicas, entrada/saída e fluxo de menus.

---

## Descrição

Market_In_Terminal é um projeto pequeno que simula um mercado no terminal. O usuário pode adicionar itens ao carrinho, visualizar a lista de compras, deletar itens e finalizar a compra. Feito para estudo e expansão — fácil de entender e customizar.

## Funcionalidades

* Adicionar itens ao carrinho.
* Visualizar a lista de compras.
* Deletar item do carrinho.
* Finalizar compras (exibe resumo e limpa o carrinho).
* Mensagens e validação simples de entradas.

## Pré-requisitos

* Python 3.8+ instalado.

## Instalação

1. Clone o repositório:

```bash
git clone https://seu-repositorio.git
cd Market_In_Terminal
```

2. (Opcional) Crie um ambiente virtual:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Não há dependências externas obrigatórias para a versão básica. Só rode com Python.

## Uso

Execute o arquivo principal:

```bash
python mercado.py
```

Ao rodar, o sistema mostra um menu semelhante a:

```text
1. Adicionar itens no carrinho.
2. Visualizar lista de compras.
3. Deletar item do carrinho.
4. Finalizar compras.
```

Fluxo comum:

* Escolha `1` para inserir um ou mais itens (ex.: separar por vírgula).
* Escolha `2` para ver o carrinho (itens numerados).
* Escolha `3` para remover: informe o número do item ou o nome.
* Escolha `4` para finalizar — o sistema exibe um resumo e encerra ou volta ao menu conforme implementação.

---

Here’s the English version:


## Market\_In\_Terminal

A simple Python system to manage a shopping cart directly from the terminal — ideal for learning basic data structures, input/output handling, and menu flows.

---

## Description

Market\_In\_Terminal is a small project that simulates a marketplace in the terminal. The user can add items to the cart, view the shopping list, delete items, and finalize the purchase.
It is built for learning and expansion — easy to understand and customize.

## Features

* Add items to the cart.
* View the shopping list.
* Delete an item from the cart.
* Finalize purchases (displays a summary and clears the cart).
* Simple input validation and messages.

## Requirements

* Python 3.8+ installed.

## Installation

1. Clone the repository:

```bash
git clone https://your-repository.git
cd Market_In_Terminal
```

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. No external dependencies are required for the basic version. Just run it with Python.

## Usage

Run the main file:

```bash
python mercado.py
```

When running, the system displays a menu similar to:

```text
1. Add items to the cart.
2. View the shopping list.
3. Delete an item from the cart.
4. Finalize purchases.
```

Typical flow:

* Choose `1` to insert one or more items (e.g., separated by commas).
* Choose `2` to view the cart (items numbered).
* Choose `3` to remove an item by its number or name.
* Choose `4` to finalize — the system displays a summary and either exits or returns to the menu, depending on the implementation.
