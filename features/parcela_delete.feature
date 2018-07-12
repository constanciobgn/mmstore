# language: pt
# Created by constanciobgn at 11/07/18

Funcionalidade: Exclusão de uma parcela de um item da lista de vendas

  Cenário: Excluir uma parcela de um item da lista de vendas criada por usuário

    Dado que existe uma venda realizada no sistema por um usuário

    Dado que existe uma parcela cadastrada para a venda realizada

    Quando o usuário clicar no link de excluir a parcela

    Então ele percebe que a parcela foi excluída da lista de parcelas