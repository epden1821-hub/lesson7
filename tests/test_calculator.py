import pytest
from pages.calculator_page import CalculatorPage


class TestCalculator:
    @pytest.fixture(autouse=True)
    def setup(self, chrome_driver):
        self.driver = chrome_driver
        self.calculator = CalculatorPage(self.driver)
        self.calculator.open()
        yield
        self.driver.quit()
    
    def test_slow_calculator(self):
        """Тест медленного калькулятора"""
        # Устанавливаем задержку
        self.calculator.set_delay(45)
        
        # Выполняем операцию 7 + 8
        self.calculator.click_button("7")
        self.calculator.click_button("+")
        self.calculator.click_button("8")
        self.calculator.click_button("=")
        
        # Ожидаем результат через 45 секунд
        result = self.calculator.wait_for_result("15", timeout=50)
        
        # Проверяем результат
        assert result == "15", f"Ожидался результат 15, получен {result}"