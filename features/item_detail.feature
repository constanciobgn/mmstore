# language: pt
# Created by constanciobgn at 03/07/18

Funcionalidade: Detalhar um venda realizada

  Cenário: Detalhar uma venda realizada sem parcelas

    Dado que existe uma venda realizada no sistema por um usuário

    Quando o usuário clicar no link de detalhar a venda

    Então ele verá os detalhes da venda


  Cenário: Detalhar uma venda realizada com parcelas

    Dado que existe uma venda realizada no sistema por um usuário

    Dado que existe uma parcela cadastrada para a venda realizada

    Quando o usuário clicar no link de detalhar a venda

    Então ele verá os detalhes da venda e da parcela cadastrada