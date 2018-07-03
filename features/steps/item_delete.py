import time

from behave import when, then
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


@when(u'o usuário clicar no link de excluir a venda')
def step_impl(context):
    context.browser.find_element_by_link_text('Excluir').click()


@then(u'ele percebe que sua venda foi excluída da lista de vendas')
def step_impl(context):
    with context.test.assertRaises(AssertionError):
        wait_for_row_in_list_table(context, 'id_item_list_table',
                                   '1 Blusa vermelha Nalveira 50,00 0 29 de Junho de 2018 Recebendo Parcelar | Detalhar | Excluir | Editar')
