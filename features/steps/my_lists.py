from behave import given, then, when
from django.conf import settings
from django.contrib.auth import get_user_model, SESSION_KEY, BACKEND_SESSION_KEY
from django.contrib.sessions.backends.db import SessionStore
from features.steps.utils import wait_to_be_logged_in, wait_to_be_logged_out
from features.steps.utils import wait_for_row_in_list_table
User = get_user_model()

def create_pre_authenticated_session(context, email):
    user = User.objects.create(email=email)
    session = SessionStore()
    session[SESSION_KEY] = user.pk
    session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
    session.save()

    context.browser.get(context.get_url('/404_no_such_url/'))
    context.browser.add_cookie(dict(name=settings.SESSION_COOKIE_NAME, value=session.session_key, path='/',))


@given(u'que existe um usuário que já se logou no sistema com o email "{email}"')
def step_impl(context, email):
    context.browser.get(context.get_url('/core/'))
    wait_to_be_logged_out(context, email)

    create_pre_authenticated_session(context, email)
    context.browser.get(context.get_url('/core/'))
    wait_to_be_logged_in(context, email)
    

@when(u'o usuário do email "{email}" faz logout no sistema')
def step_impl(context, email):
    logout = context.browser.find_element_by_link_text('Log out')
    context.test.assertTrue(logout.is_displayed())
    logout.click()
    wait_to_be_logged_out(context, email)


# @then(u'ele não consegue mais visualizar as vendas')
# def step_impl(context):
#     with context.test.assertRaises(AssertionError):
#         wait_for_row_in_list_table(context, 'id_item_list_table',
#                                    '1 Blusa vermelha Nalveira 50,00 0 29 de Junho de 2018 Recebendo Parcelar | Detalhar | Excluir | Editar')
