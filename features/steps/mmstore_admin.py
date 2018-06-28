import time

from behave import when, then
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10


@when(u'o usuário acessa a url "{url}" relativa a criação de lista de vendas')
def step_impl(context, url):
    context.browser.get(context.get_url(url))


@when(u'insere "Blusa vermelha" no campo de descrição da venda')
def step_impl(context):
    context.browser.find_element_by_id('id_descricao').send_keys('Blusa vermelha')


@when(u'insere "50" no campo do valor da compra')
def step_impl(context):
    context.browser.find_element_by_id('id_valor_compra').send_keys('50')


@when(u'Clica no botão de salvar a venda')
def step_impl(context):
    context.browser.find_element_by_id('id_btn_salvar').click()


@then(u'ele percebe que sua venda foi inserida na lista de vendas')
def step_impl(context):
    start_time = time.time()
    while True:
        try:
            table = context.browser.find_element_by_id('id_list_table')
            rows = table.find_elements_by_tag_name('tr')
            context.test.assertIn('1: Blusa vermelha 50,00', [row.text for row in rows])
            return
        except (AssertionError, WebDriverException) as e:
            if time.time() - start_time > MAX_WAIT:
                raise e
            time.sleep(0.5)
