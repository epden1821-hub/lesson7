from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
    
    def fill_checkout_form(self, first_name, last_name, postal_code):
        """Заполняет форму оформления заказа"""
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()
    
    def get_total_price(self):
        """Возвращает итоговую стоимость"""
        total_element = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        return total_element.text.replace("Total: $", "")
    
    def finish_checkout(self):
        """Завершает оформление заказа"""
        self.driver.find_element(By.ID, "finish").click()