from behave import given, when, then


@given(u'que existe um usuário qualquer acessando o site da loja MMStore')
def step_impl(context):
    assert context.browser


@when(u'o usuário acessa a url "{url}"')
def step_impl(context, url):
    context.browser.get(context.get_url(url))


@then(u'ele visualiza a mensagem "Hello World"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then ele visualiza a mensagem "Hello World"')
