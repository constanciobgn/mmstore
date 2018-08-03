# # language: pt
# # Created by constanciobgn at 13/07/18

# Funcionalidade: Logar e logout no sistema

#   Cenário: Login de um usuário no sistema

#     Dado que existe um usuário qualquer acessando o site da loja MMStore

#     Quando o usuário acessa a url "/core/"

#     E inserir o email "user@exemplo.com" na caixa de texto

#     E clicar no link "Entrar"

#     Então uma mensagem aparece informando-lhe que um email foi enviado

#     Então ele verifica sua caixa de email e encontra a mensagem

#     E a mensagem contém um link com um url

#     Então ele clica no link do email

#     E loga-se no sistema


#   Cenário: Logout de um usuário no sistema

#     Dado que existe um usuário logado no site da loja MMStore

#     Quando ele clica no link de logout

#     Então ele não está mais logado
    