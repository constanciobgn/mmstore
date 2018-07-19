# language: pt
# Created by constanciobgn at 11/07/18

Funcionalidade: Edição de uma parcela de um item da lista de vendas

  Cenário: Editar uma parcela de um item da lista de vendas criada por usuário

    Dado que existe uma venda realizada no sistema por um usuário

    Dado que existe uma parcela cadastrada para a venda realizada

    Quando o usuário clicar no link de detalhar a venda

    Quando o usuário clicar no link de editar a parcela

    Então ele será redirecionado para a página de edição da parcela

    Quando ele corregir as informações incorretas na página de edição da parcela

    E Clica no botão de salvar a parcela

    Então ele percebe que a parcela foi editada da lista de parcelas