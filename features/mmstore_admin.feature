# language: pt
# Created by constanciobgn at 28/06/18

Funcionalidade: Implementação da parte administrativa da loja MMStore


  Cenário: Criação de uma nova lista de vendas para um usuário

    Dado que existe um usuário qualquer acessando o site da loja MMStore

    Quando o usuário acessa a url "/core/" relativa a criação de lista de vendas

    E insere "Blusa vermelha" no campo de descrição da venda

    E insere "50" no campo do valor da compra

    E insere "29/06/2018" no campo da data de venda

    E Clica no botão de salvar a venda

    E insere "Recebendo" no campo de status da venda

    Então ele percebe que sua venda foi inserida na lista de vendas

  Cenário: Adição de uma parcela em uma venda realizada

    Dado que existe uma venda realizada no sistema por um usuário

    Quando o usuário clicar no link de adicionar parcela na venda

    E inserir "29/06/2018" no campo da data de recebimento da parcela

    E inserir "25" no campo do valor da parcela

    E inserir "Pendente" no campo de status da parcela

    E Clica no botão de salvar a parcela

    Então ele percebe que a parcela foi inserida na venda


  Cenário: Detalhar uma venda realizada sem parcelas

    Dado que existe uma venda realizada no sistema por um usuário

    Quando o usuário clicar no link de detalhar a venda

    Então ele verá os detalhes da venda


