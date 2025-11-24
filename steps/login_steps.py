import time
from behave import given, when, then


@then('el titulo contiene "{texto}"')
def step_title(context, texto):
    context.login_screen.assert_title_contains(texto)
    time.sleep(2)


@given('que abro el navegador en la página de login') 
def step_open_login(context):
        context.login_screen.open()    


@when('inicion de sesion con "{usuario}" y "{password}"')
def step_login(context, usuario, password):
    context.login_screen.login(usuario, password)  
    time.sleep(2)  


@then('el resultado debe ser "{resultado}"')
def step_login(context, resultado):
    context.login_screen.assert_login_result(resultado)    
    time.sleep(2)