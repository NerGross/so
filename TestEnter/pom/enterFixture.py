import allure
import config
from TestEnter.pom.enterLocator import EnterLocator


class EnterVFixture:
    def __init__(self):
        self.driver = None

    def enter_SK(self):
        """Логин пароль в ЛК для сотрудника куратор"""
        enter = EnterLocator(self.driver)
        with allure.step("Загрузки страницы ввода логина и пароля"):
            enter.get_button("Войти")
        with allure.step('Вход в ЛК'):
            enter.get_auth("Логин").send_keys(config.enter["l_curator"])
            enter.get_auth("Пароль").send_keys(config.enter["p_curator"])
            enter.get_button("Войти").click()
        with allure.step("Загрузки страницы выбор компании"):
            enter.get_not_button("Войти")
            assert enter.get_drop_down_meaning("Страхование ТС")

    def enter_SS(self):
        """Логин пароль в ЛК для сотрудника страхователя"""
        enter = EnterLocator(self.driver)
        with allure.step("Загрузки страницы ввода логина и пароля"):
            enter.get_button("Войти")
        with allure.step('Вход в ЛК'):
            enter.get_auth("Логин").send_keys(config.enter["l_employee"])
            enter.get_auth("Пароль").send_keys(config.enter["p_employee"])
            enter.get_button("Войти").click()
        with allure.step("Загрузки страницы выбор компании"):
            enter.get_not_button("Войти")
            assert enter.get_drop_down_meaning("Страхование ТС")

    def transition_to_vehicle(self):
        enter = EnterLocator(self.driver)
        with allure.step('Переход по меню'):
            enter.get_menu("Объекты страхования").click()
            enter.get_menu("Транспортные средства").click()
        with allure.step("Транспортные средства"):
            enter.get_not_drop_down_meaning("Страхование ТС")
