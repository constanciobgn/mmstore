@when(u'o usuário acessa a url "{url}" relativa ao dashboard')
def step_impl(context, url):
    context.browser.get(context.get_url(url))

@then(u'ele nota Dashboard no título da página')
def step_impl(context):
    titulo = context.browser.title
    context.test.assertIn('Dashboard', titulo)