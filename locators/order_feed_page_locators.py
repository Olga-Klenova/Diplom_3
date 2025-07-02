from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    FEED_TITLE = (By.XPATH, ".//h1[text()='Лента заказов']")  # заголовок формы ленты заказов "Лента заказов"

    FIRS_ORDER_CARD_IN_FEED = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[1]") # первая карточка в ленте заказов

    ORDER_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]") # модальное окно на странице заказов

    ORDER_TEXT_IN_ORDER_MODAL = (By.XPATH, "//p[text()= 'Cостав']") # текст состава в открытом модальном окне

    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p") # общее кол-во заказов

    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p") # кол-во заказов выполненных сегодня

    ALL_ORDERS_IN_FEED = (By.XPATH, "//p[starts-with(text(),'#')]") # все заказы в ленте заказов

    ALL_ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'digits')]") # все заказы в работе