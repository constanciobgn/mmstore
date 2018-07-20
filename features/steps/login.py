import re
import time

from behave import when, then
from django.core import mail

TEST_EMAIL = 'user@exemplo.com'
SUBJECT = 'Your login link for MMStore'


@when(u'inserir o email "user@exemplo.com" na caixa de texto')
def step_impl(context):
    context.inputmail = context.browser.find_element_by_id('id_email')
    context.test.assertTrue(context.inputmail.is_displayed())
    context.inputmail.send_keys(TEST_EMAIL)


@when(u'clicar no link "Entrar"')
def step_impl(context):
    btn_login = context.browser.find_element_by_id('id_btn_login')
    context.test.assertTrue(btn_login.is_displayed())
    btn_login.click()


@then(u'uma mensagem aparece informando-lhe que um email foi enviado')
def step_impl(context):
    time.sleep(1)
    context.test.assertIn('Check your email', context.browser.find_element_by_tag_name('body').text)


@then(u'ele verifica sua caixa de email e encontra a mensagem')
def step_impl(context):
    context.email = mail.outbox[0]
    context.test.assertIn(TEST_EMAIL, context.email.to)
    context.test.assertEqual(context.email.subject, SUBJECT)


@then(u'a mensagem contém um link com um url')
def step_impl(context):
    context.test.assertIn('Use this link to log in', context.email.body)
    url_search = re.search(r'http://.+/.+$', context.email.body)
    if not url_search:
        context.test.fail(f'Could not find url in email body:\n{email.body}')
    context.url = url_search.group(0)
    context.test.assertIn('localhost', context.url)


@then(u'ele clica no link do email')
def step_impl(context):
    context.browser.get(context.url)


@then(u'loga-se no sistema')
def step_impl(context):
    navbar = context.browser.find_element_by_css_selector('p')
    context.test.assertIn(TEST_EMAIL, navbar.text)
