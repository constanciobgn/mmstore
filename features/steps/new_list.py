import time

from behave import when, then
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

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


@when(u'insere "Nalveira" no campo de cliente da compra')
def step_impl(context):
    context.browser.find_element_by_id('id_cliente').send_keys('Nalveira')


@when(u'insere "50" no campo do valor da compra')
def step_impl(context):
    context.browser.find_element_by_id('id_valor_compra').send_keys('50')


@when(u'insere "29/06/2018" no campo da data de venda')
def step_impl(context):
    context.browser.find_element_by_id('id_data_venda').clear()
    context.browser.find_element_by_id('id_data_venda').send_keys('29/06/2018')
    context.browser.find_element_by_id('id_data_venda').send_keys(Keys.TAB)


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
                               '1 Blusa vermelha Nalveira 50,00 0 29 de Junho de 2018 Recebendo Parcelar | Detalhar | Excluir | Editar')
