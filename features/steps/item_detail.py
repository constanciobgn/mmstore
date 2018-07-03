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


@when(u'o usuário clicar no link de detalhar a venda')
def step_impl(context):
    context.browser.find_element_by_link_text('Detalhar').click()


@then(u'ele verá os detalhes da venda')
def step_impl(context):
    wait_for_row_in_list_table(context, 'id_item_list_table',
                               'Blusa vermelha Nalveira 50,00 0 29 de Junho de 2018 Recebendo Parcelar')


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
                               'Blusa vermelha Nalveira 50,00 25,00 29 de Junho de 2018 Recebendo Parcelar')
    wait_for_row_in_list_table(context, 'id_parcela_list_table', '1 29 de Junho de 2018 25,00 Pendente')
