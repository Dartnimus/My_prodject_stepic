from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def go_to_login_page(browser):
    link = browser.find_element_by_css_selector("#login_link")
    link.click()


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    #page.should_be_login_link()      # проверяем существование ссылки ведущей к логину
    #page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
