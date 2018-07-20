from behave import when, then

@when(u'o usuário acessa a url "{url}" relativa a landing page')
def step_impl(context, url):
    context.browser.get(context.get_url(url))

@then(u'ele nota MMStore no título da página')
def step_impl(context):
    titulo = context.browser.title
    context.test.assertIn('MMStore', titulo)


