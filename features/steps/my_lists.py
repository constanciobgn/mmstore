from behave import given
from django.conf import settings
from django.contrib.auth import get_user_model, SESSION_KEY, BACKEND_SESSION_KEY
from django.contrib.sessions.backends.db import SessionStore
User = get_user_model()

@given(u'que existe um usuário que já se logou no sistema com o email "{email}"')
def step_impl(context, email):
    user = User.objects.create(email=email)
    session = SessionStore()
    session[SESSION_KEY] = user.pk
    session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
    session.save()

    context.browser.get(context.get_url('/404_no_such_url/'))
    context.browser.add_cookie(dict(name=settings.SESSION_COOKIE_NAME, value=session.session_key, path='/',))