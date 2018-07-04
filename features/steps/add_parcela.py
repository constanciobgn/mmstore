from behave import when, then, given
from selenium.webdriver.common.keys import Keys

from features.steps.utils import wait_for_row_in_list_table


@given(u'que existe uma venda realizada no sistema por um usuário')
def step_impl(context):
    context.browser.get(context.get_url('/core/'))
    context.browser.find_element_by_id('id_descricao').send_keys('Blusa vermelha')
    context.browser.find_element_by_id('id_cliente').send_keys('Nalveira')
    context.browser.find_element_by_id('id_valor_compra').send_keys('50')
    context.browser.find_element_by_id('id_data_venda').clear()
    context.browser.find_element_by_id('id_data_venda').send_keys('29/06/2018')
    context.browser.find_element_by_id('id_data_venda').send_keys(Keys.TAB)
    context.browser.find_element_by_id('id_status').send_keys('0')
    context.browser.find_element_by_id('id_btn_salvar').click()
    wait_for_row_in_list_table(context, 'id_item_list_table',
                               '1 Blusa vermelha Nalveira 50,00 0 29 de Junho de 2018 Recebendo Parcelar | Detalhar | Excluir | Editar')


@when(u'o usuário clicar no link de adicionar parcela na venda')
def step_impl(context):
    link_parcela = context.browser.find_element_by_link_text('Parcelar')
    context.test.assertTrue(link_parcela.is_displayed())
    link_parcela.click()


@when(u'inserir "29/06/2018" no campo da data de recebimento da parcela')
def step_impl(context):
    context.browser.find_element_by_id('id_data_recebimento').clear()
    context.browser.find_element_by_id('id_data_recebimento').send_keys('29/06/2018')


@when(u'inserir "25" no campo do valor da parcela')
def step_impl(context):
    context.browser.find_element_by_id('id_valor').send_keys('25')


@when(u'inserir "Pendente" no campo de status da parcela')
def step_impl(context):
    context.test.assertTrue(context.browser.find_element_by_id('id_status').is_displayed)
    context.browser.find_element_by_id('id_status').send_keys('0')


@when(u'Clica no botão de salvar a parcela')
def step_impl(context):
    context.browser.find_element_by_id('id_btn_salvar').click()


@then(u'ele percebe que a parcela foi inserida na venda')
def step_impl(context):
    wait_for_row_in_list_table(context, 'id_parcela_list_table', '1 29 de Junho de 2018 25,00 Pendente')
