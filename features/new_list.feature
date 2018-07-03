# language: pt
# Created by constanciobgn at 03/07/18

Funcionalidade: Criação de uma lista de vendas

  Cenário: Nova lista de vendas para um usuário

    Dado que existe um usuário qualquer acessando o site da loja MMStore

    Quando o usuário acessa a url "/core/" relativa a criação de lista de vendas

    E insere "Blusa vermelha" no campo de descrição da venda

    E insere "Nalveira" no campo de cliente da compra

    E insere "50" no campo do valor da compra

    E insere "29/06/2018" no campo da data de venda

    E insere "Recebendo" no campo de status da venda

    E Clica no botão de salvar a venda

    Então ele percebe que sua venda foi inserida na lista de vendas

