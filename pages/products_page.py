from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
    
    def add_to_cart(self, product_name):
        """Добавляет товар в корзину по названию"""
        # Находим все товары
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        
        for product in products:
            name_element = product.find_element(By.CLASS_NAME, "inventory_item_name")
            if product_name in name_element.text:
                add_button = product.find_element(By.CSS_SELECTOR, "button")
                add_button.click()
                return
    
    def go_to_cart(self):
        """Переходит в корзину"""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    def get_cart_count(self):
        """Возвращает количество товаров в корзине"""
        cart_badge = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        return int(cart_badge[0].text) if cart_badge else 0