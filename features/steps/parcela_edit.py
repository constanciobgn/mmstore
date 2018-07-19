from behave import when, then

from features.steps.utils import wait_for_row_in_list_table


@when(u'o usuário clicar no link de editar a parcela')
def step_impl(context):
    context.browser.find_element_by_link_text('Editar').click()


@then(u'ele será redirecionado para a página de edição da parcela')
def step_impl(context):
    context.test.assertRegex(context.browser.current_url, 'core/lists/(\d+)/items/(\d+)/parcelas/(\d+)/parcela_edit')


@when(u'ele corregir as informações incorretas na página de edição da parcela')
def step_impl(context):
    context.browser.find_element_by_id('id_valor').clear()
    context.browser.find_element_by_id('id_valor').send_keys('34')


@then(u'ele percebe que a parcela foi editada da lista de parcelas')
def step_impl(context):
    wait_for_row_in_list_table(context, 'id_parcela_list_table', '1 29 de Junho de 2018 34,00 Pendente Excluir | Editar')
