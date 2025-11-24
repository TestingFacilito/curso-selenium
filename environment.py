from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from screens.login_screen import LoginScreen

def before_scenario(context, driver):
    options = Options()
    #options.add_argument('--headless=new')
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    context.login_screen = LoginScreen(context.driver)

def after_scenario(context, driver):
    context.driver.quit()

