# language: pt
# Created by constanciobgn at 03/07/18

Funcionalidade: Exclusão de um item da lista de vendas

  Cenário: Excluir um item sem parcelas de uma lista de vendas criada por usuário

    Dado que existe uma venda realizada no sistema por um usuário

    Quando o usuário clicar no link de excluir a venda

    Então ele percebe que sua venda foi excluída da lista de vendas