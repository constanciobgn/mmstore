# language: pt
# Created by constanciobgn at 05/07/18

Funcionalidade: Listar vendas com parcelas atrasadas

  Cenário: Lista de vendas com parcelas atrasadas

    Dado que existe um usuário qualquer acessando o site da loja MMStore

    Dado que existe uma venda realizada no sistema por um usuário

    Dado que existe uma parcela cadastrada para a venda com data de recebimento menor que a data atual

    Quando o usuário acessa a url "/core/" relativa a criação de lista de vendas

    Então ele percebe que sua venda está na lista de vendas com parcelas em atraso