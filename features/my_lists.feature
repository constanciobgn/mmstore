Feature: Atribuir listas de vendas para um usuário
    
    Scenario: Criação de uma lista de venda para um usuário logado no sistema
    
        Given que existe um usuário que já se logou no sistema com o email "edith@example.com"

        Given que existe uma venda realizada no sistema por um usuário

    Scenario: Usuário não logado não consegue ver lista de vendas

        Given que existe um usuário que já se logou no sistema com o email "edith@example.com"

        Given que existe uma venda realizada no sistema por um usuário

        When o usuário do email "edith@example.com" faz logout no sistema

        # Then ele não consegue mais visualizar as vendas

    
    

    