from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
    
    def click_checkout(self):
        """Нажимает кнопку Checkout"""
        self.driver.find_element(By.ID, "checkout").click()
    
    def get_cart_items(self):
        """Возвращает список товаров в корзине"""
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return [item.find_element(By.CLASS_NAME, "inventory_item_name").text for item in items]