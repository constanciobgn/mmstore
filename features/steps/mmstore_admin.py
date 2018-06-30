import time

from behave import when, then, given
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10


def wait_for_row_in_list_table(context, id_table, row_text):
    start_time = time.time()
    while True:
        try:
            table = context.browser.find_element_by_id(id_table)
            rows = table.find_elements_by_tag_name('tr')
            context.test.assertIn(row_text, [row.text for row in rows])
            return
        except (AssertionError, WebDriverException) as e:
            if time.time() - start_time > MAX_WAIT:
                raise e
            time.sleep(0.5)


@when(u'o usuário acessa a url "{url}" relativa a criação de lista de vendas')
def step_impl(context, url):
    context.browser.get(context.get_url(url))


@when(u'insere "Blusa vermelha" no campo de descrição da venda')
def step_impl(context):
    context.browser.find_element_by_id('id_descricao').send_keys('Blusa vermelha')


@when(u'insere "50" no campo do valor da compra')
def step_impl(context):
    context.browser.find_element_by_id('id_valor_compra').send_keys('50')


@when(u'insere "29/06/2018" no campo da data de venda')
def step_impl(context):
    context.browser.find_element_by_id('id_data_venda').clear()
    context.browser.find_element_by_id('id_data_venda').send_keys('29/06/2018')


@when(u'insere "Recebendo" no campo de status da venda')
def step_impl(context):
    context.test.assertTrue(context.browser.find_element_by_id('id_status').is_displayed)
    context.browser.find_element_by_id('id_status').send_keys('0')


@when(u'Clica no botão de salvar a venda')
def step_impl(context):
    context.browser.find_element_by_id('id_btn_salvar').click()


@then(u'ele percebe que sua venda foi inserida na lista de vendas')
def step_impl(context):
    wait_for_row_in_list_table(context, 'id_item_list_table',
                               '1 Blusa vermelha 50,00 29 de Junho de 2018 Recebendo Parcelar | Detalhar')


@given(u'que existe uma venda realizada no sistema por um usuário')
def step_impl(context):
    context.browser.get(context.get_url('/core/'))
    context.browser.find_element_by_id('id_descricao').send_keys('Blusa vermelha')
    context.browser.find_element_by_id('id_valor_compra').send_keys('50')
    context.browser.find_element_by_id('id_data_venda').clear()
    context.browser.find_element_by_id('id_data_venda').send_keys('29/06/2018')
    context.browser.find_element_by_id('id_status').send_keys('0')
    context.browser.find_element_by_id('id_btn_salvar').click()
    wait_for_row_in_list_table(context, 'id_item_list_table',
                               '1 Blusa vermelha 50,00 29 de Junho de 2018 Recebendo Parcelar | Detalhar')


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


@when(u'o usuário clicar no link de detalhar a venda')
def step_impl(context):
    context.browser.find_element_by_link_text('Detalhar').click()


@then(u'ele verá os detalhes da venda')
def step_impl(context):
    wait_for_row_in_list_table(context, 'id_item_list_table',
                               'Blusa vermelha 50,00 29 de Junho de 2018 Recebendo Parcelar')


@given(u'que existe uma parcela cadastrada para a venda realizada')
def step_impl(context):
    link_parcela = context.browser.find_element_by_link_text('Parcelar')
    context.test.assertTrue(link_parcela.is_displayed())
    link_parcela.click()
    context.browser.find_element_by_id('id_data_recebimento').clear()
    context.browser.find_element_by_id('id_data_recebimento').send_keys('29/06/2018')
    context.browser.find_element_by_id('id_valor').send_keys('25')
    context.test.assertTrue(context.browser.find_element_by_id('id_status').is_displayed)
    context.browser.find_element_by_id('id_status').send_keys('0')
    context.browser.find_element_by_id('id_btn_salvar').click()
    wait_for_row_in_list_table(context, 'id_parcela_list_table', '1 29 de Junho de 2018 25,00 Pendente')
    context.browser.get(context.get_url('/core/'))


@then(u'ele verá os detalhes da venda e da parcela cadastrada')
def step_impl(context):
    wait_for_row_in_list_table(context, 'id_item_list_table',
                               'Blusa vermelha 50,00 29 de Junho de 2018 Recebendo Parcelar')
    wait_for_row_in_list_table(context, 'id_parcela_list_table', '1 29 de Junho de 2018 25,00 Pendente')
