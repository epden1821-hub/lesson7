import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestSauceDemo:
    @pytest.fixture(autouse=True)
    def setup(self, firefox_driver):
        self.driver = firefox_driver
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        yield
        self.driver.quit()
    
    def test_complete_purchase(self):
        """Тест полного процесса покупки"""
        # 1. Открываем сайт и авторизуемся
        self.login_page.open()
        self.login_page.login("standard_user", "secret_sauce")
        
        # 2. Добавляем товары в корзину
        self.products_page.add_to_cart("Sauce Labs Backpack")
        self.products_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        self.products_page.add_to_cart("Sauce Labs Onesie")
        
        # Проверяем, что в корзине 3 товара
        cart_count = self.products_page.get_cart_count()
        assert cart_count == 3, f"Ожидалось 3 товара в корзине, получено {cart_count}"
        
        # 3. Переходим в корзину
        self.products_page.go_to_cart()
        
        # Проверяем, что товары добавлены
        cart_items = self.cart_page.get_cart_items()
        expected_items = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
        
        for item in expected_items:
            assert any(item in cart_item for cart_item in cart_items), f"Товар {item} не найден в корзине"
        
        # 4. Нажимаем Checkout
        self.cart_page.click_checkout()
        
        # 5. Заполняем форму данными
        self.checkout_page.fill_checkout_form("Ivan", "Ivanov", "123456")
        
        # 6. Получаем итоговую стоимость
        total_price = self.checkout_page.get_total_price()
        
        # 7. Проверяем итоговую стоимость
        expected_total = "58.29"
        assert total_price == expected_total, f"Ожидалась сумма ${expected_total}, получена ${total_price}"
        
        # 8. Завершаем покупку (опционально)
        self.checkout_page.finish_checkout()