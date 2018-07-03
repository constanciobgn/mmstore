# language: pt
# Created by constanciobgn at 28/06/18

Funcionalidade: Edição de um item da lista de vendas

  Cenário: Editar um item sem parcelas de uma lista de vendas criada por usuário

    Dado que existe uma venda realizada no sistema por um usuário

    Quando o usuário clicar no link de editar a venda

    Então ele será redirecionado para a página de edição do item

    Quando ele corregir as informações incorretas na página de edição do item

    E Clica no botão de salvar a venda

    Então ele percebe que sua venda foi editada na lista de vendas