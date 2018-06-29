# language: pt

Funcionalidade: Apresentar a mensagem "Hello World" na tela

  Cenário: Acesso a url "/hello/" do site da loja MMStore

    Dado que existe um usuário qualquer acessando o site da loja MMStore

    Quando o usuário acessa a url "/hello/"

    Então ele visualiza a mensagem "Hello World"


