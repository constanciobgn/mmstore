# language: pt
# Created by constanciobgn at 03/07/18

Funcionalidade: Adição de uma parcela em um item da lista de venda

  Cenário: Adição de uma parcela em uma venda realizada

    Dado que existe uma venda realizada no sistema por um usuário

    Quando o usuário clicar no link de adicionar parcela na venda

    E inserir "29/06/2018" no campo da data de recebimento da parcela

    E inserir "25" no campo do valor da parcela

    E inserir "Pendente" no campo de status da parcela

    E Clica no botão de salvar a parcela

    Então ele percebe que a parcela foi inserida na venda