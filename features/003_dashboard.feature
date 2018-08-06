# language: pt

Funcionalidade: Exibir o Dashboard da loja MMStore

  Cenário: Acesso de um usuário qualquer ao dashboard da loja MMStore

    Dado que existe um usuário qualquer acessando o site da loja MMStore

    Quando o usuário acessa a url "/dashboard/" relativa ao dashboard

    Então ele nota Dashboard no título da página
