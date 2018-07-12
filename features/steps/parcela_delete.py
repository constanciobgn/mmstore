from behave import when, then

from features.steps.utils import wait_for_row_in_list_table


@when(u'o usuário clicar no link de excluir a parcela')
def step_impl(context):
    context.browser.find_element_by_link_text('Excluir').click()


@then(u'ele percebe que a parcela foi excluída da lista de parcelas')
def step_impl(context):
    with context.test.assertRaises(AssertionError):
        wait_for_row_in_list_table(context, 'id_parcela_list_table', '1 29 de Junho de 2018 25,00 Pendente Excluir')

