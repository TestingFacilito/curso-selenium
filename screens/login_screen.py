from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginScreen:
    LOGIN_URL = "https://www.saucedemo.com/"
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON   = (By.ID, 'login-button')
    ERROR_MESSAGE  = (By.CSS_SELECTOR, "[data-test='error']")
    INVENTORY_TITLE  = (By.CSS_SELECTOR, 'span.title')

    def open(self):
        self.driver.get(self.LOGIN_URL)
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON))


    def login(self, username, password):
        user = self.driver.find_element(*self.USERNAME_INPUT)
        pwd = self.driver.find_element(*self.PASSWORD_INPUT)
        btn = self.driver.find_element(*self.LOGIN_BUTTON)

        user.clear()
        user.send_keys(username)
        pwd.clear()
        pwd.send_keys(password)
        btn.click()

    def assert_title_contains(self, text):
        assert text.lower() in self.driver.title.lower(), \
            f'El título "{self.driver.title}" no contiene "{text}"'
    
    def assert_login_result(self, resultado):
        if resultado == "success":
            self.wait.until(EC.url_contains("/inventory.html"))
            title = self.wait.until(EC.visibility_of_element_located(self.INVENTORY_TITLE))
            assert title.text.strip().lower() == "products", "No se mostró Products"
        elif resultado in ("locked", "badcreds"):
            err = self.wait.until(
                EC.visibility_of_element_located((self.ERROR_MESSAGE))
            )
            msg = err.text.strip().lower()
            if (resultado == "locked"):
                assert "locked out" in msg, f"Mensaje no indica usuario bloqueado: {msg}"
            else:
                assert "do not match" in msg or "epic sadface" in msg, f"Mensaje inesperado: {msg}"
        else:
            raise AssertionError(f"Resultado desconocido: {resultado}")
