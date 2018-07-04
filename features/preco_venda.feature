# language: pt
# Created by constanciobgn at 03/07/18

Funcionalidade: Calcular preço de venda de um determinado item

  Cenário: Cálculo do preço de venda de um item

    Dado que existe um usuário qualquer acessando o site da loja MMStore

    Quando ele clicar no link "Preços" dentro do submenu "Plugins"

    Então ele será redirecionado para a página de cálculo de preços

    Quando ele insere "150" no campo de preço

    E clica no botão "Calcular"

    Então ele verá um lista de preços para algumas porcentagens predeterminadas