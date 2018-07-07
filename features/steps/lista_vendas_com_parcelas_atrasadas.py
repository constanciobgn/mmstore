from behave import given, then
from datetime import date, timedelta

from features.steps.utils import wait_for_row_in_list_table


@given(u'que existe uma parcela cadastrada para a venda com data de recebimento menor que a data atual')
def step_impl(context):
    link_parcela = context.browser.find_element_by_link_text('Parcelar')
    context.test.assertTrue(link_parcela.is_displayed())
    link_parcela.click()

    context.browser.find_element_by_id('id_data_recebimento').clear()
    context.browser.find_element_by_id('id_data_recebimento').send_keys(f'{ (date.today() - timedelta(days=2)).strftime("%d/%m/%Y") }')

    context.browser.find_element_by_id('id_valor').send_keys('25')

    context.test.assertTrue(context.browser.find_element_by_id('id_status').is_displayed)
    context.browser.find_element_by_id('id_status').send_keys('0')

    context.browser.find_element_by_id('id_btn_salvar').click()

    wait_for_row_in_list_table(context, 'id_parcela_list_table', '1 5 de Julho de 2018 25,00 Pendente')


@then(u'ele percebe que sua venda está na lista de vendas com parcelas em atraso')
def step_impl(context):
    context.browser.get(context.get_url('/core/'))
    wait_for_row_in_list_table(context, 'id_lista_vendas_com_parcelas_atrasadas',
                               '1 Blusa vermelha Nalveira 50,00 25,00 29 de Junho de 2018 Recebendo Parcelar | Detalhar | Excluir | Editar')
