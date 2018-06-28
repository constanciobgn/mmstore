# language: pt
# Created by constanciobgn at 28/06/18

  Funcionalidade: Implementação da parte administrativa da loja MMStore

    Cenário: Criação de uma nova lista de vendas para um usuário

      Dado que existe um usuário qualquer acessando o site da loja MMStore

      Quando o usuário acessa a url "/core/" relativa a criação de lista de vendas

      E insere "Blusa vermelha" no campo de descrição da venda

      E insere "50" no campo do valor da compra

      E Clica no botão de salvar a venda

      Então ele percebe que sua venda foi inserida na lista de vendas

