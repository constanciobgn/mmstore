from behave import when, then

from features.steps.utils import wait_for_row_in_list_table


@when(u'o usuário clicar no link de editar a venda')
def step_impl(context):
    context.browser.find_element_by_link_text('Editar').click()


@then(u'ele será redirecionado para a página de edição do item')
def step_impl(context):
    context.test.assertRegex(context.browser.current_url, 'core/lists/(\d+)/items/(\d+)/item_edit')


@when(u'ele corregir as informações incorretas na página de edição do item')
def step_impl(context):
    context.browser.find_element_by_id('id_descricao').clear()
    context.browser.find_element_by_id('id_descricao').send_keys('Blusa azul')


@then(u'ele percebe que sua venda foi editada na lista de vendas')
def step_impl(context):
    wait_for_row_in_list_table(context, 'id_item_list_table',
                               '1 Blusa azul Nalveira 50,00 0 29 de Junho de 2018 Recebendo Parcelar | Detalhar | Excluir | Editar')
