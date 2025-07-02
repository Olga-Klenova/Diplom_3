from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = None # Должен быть задан в дочерних классах

    def open(self):
        self.driver.get(self.url)

    def fill_input(self, locator, text): # подождать инпут и ввести значение
        self.wait_visibility_of_element(locator)
        self.driver.find_element(*locator).send_keys(text)

    def wait_visibility_of_element(self, locator): # ждет пока элемент станет видимым
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    def wait_invisibility_of_element(self, locator, timeout=10):  # ждёт, пока элемент станет невидимым
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.invisibility_of_element_located(locator)
        )

    def click_on_element(self, locator): # клик по элементу
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()


    def get_text_element(self, locator): # получить текст элемента
        return self.driver.find_element(*locator).text

    def get_texts_from_elements(self, locator):  # получить текст из всех элементов
        self.wait_visibility_of_element(locator)
        elements = self.driver.find_elements(*locator)
        number_order = []
        for item in elements:
            number_order.append(item.text.strip())
        return number_order

    def get_current_url(self, expected_url=None, timeout=10): # Получает текущий URL. Если передан expected_url, ждет его появления.
        if expected_url:
            WebDriverWait(self.driver, timeout).until(
                expected_conditions.url_to_be(expected_url)
            )
        return self.driver.current_url


    def is_disappeared(self, locator, timeout=10): # ждет исчезновения элемента из дерева
        WebDriverWait(self.driver, timeout,1).until_not(
                expected_conditions.presence_of_element_located(locator))

    def is_element_visible(self, locator): # ждет и проверяет видимость элемента на странице
        try:
            self.wait_visibility_of_element(locator)
            return True
        except TimeoutException:
            return False

    def is_modal_closed(self, locator, timeout=10): # Проверяет, что модальное окно закрылось (все попапы)
        try:
            self.is_disappeared(locator)
            return True
        except TimeoutException:
            return False

    def wait_modal_opened(self, locator): # ждем появления модального окна
        self.wait_visibility_of_element(locator)

    def wait_modal_closed(self, locator): # ждет исчезновения модального окна
        self.is_disappeared(locator)

    def scroll_to_and_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        element.click()