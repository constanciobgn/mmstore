from behave import when, then


@when(u'ele clicar no link "Preços" dentro do submenu "Plugins"')
def step_impl(context):
    context.browser.get(context.get_url('/core/'))
    context.test.assertRegex(context.browser.current_url, 'core/')

    link_precos = context.browser.find_element_by_link_text('Preços')
    context.test.assertTrue(link_precos.is_displayed())
    link_precos.click()


@then(u'ele será redirecionado para a página de cálculo de preços')
def step_impl(context):
    context.test.assertRegex(context.browser.current_url, 'core/precos/')

    input_preco = context.browser.find_element_by_id('id_preco')
    context.test.assertTrue(input_preco.is_displayed())


@when(u'ele insere "150" no campo de preço')
def step_impl(context):
    input_preco = context.browser.find_element_by_id('id_preco')
    context.test.assertTrue(input_preco.is_displayed())
    input_preco.send_keys('150')


@when(u'clica no botão "Calcular"')
def step_impl(context):
    context.browser.find_element_by_id('id_btn_calcular').click()


@then(u'ele verá um lista de preços para algumas porcentagens predeterminadas')
def step_impl(context):
    contents = [('sale_price_60', '240,00 90,00'), ('sale_price_70', '255,00 105,00'),
                ('sale_price_80', '270,00 120,00'), ('sale_price_100', '300,00 150,00')]

    result = context.browser.find_element_by_id('sale_price_60').text
    context.test.assertIn('240,00 90,00', result)

    # for content in contents:
    #     with context.test.subTest():
    #         result = context.browser.find_element_by_id(content[0]).text
    #         context.test.assertIn(result, content[1])
