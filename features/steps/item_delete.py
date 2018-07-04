from behave import when, then

from features.steps.utils import wait_for_row_in_list_table


@when(u'o usuário clicar no link de excluir a venda')
def step_impl(context):
    context.browser.find_element_by_link_text('Excluir').click()


@then(u'ele percebe que sua venda foi excluída da lista de vendas')
def step_impl(context):
    with context.test.assertRaises(AssertionError):
        wait_for_row_in_list_table(context, 'id_item_list_table',
                                   '1 Blusa vermelha Nalveira 50,00 0 29 de Junho de 2018 Recebendo Parcelar | Detalhar | Excluir | Editar')
