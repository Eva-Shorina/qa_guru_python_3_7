import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from allure_commons.types import Severity

@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'eva.shorina')
@allure.feature('Issues в репозитории')
@allure.story('Проверка номера issue')
@allure.link('https://github.com', name='Testing')
def test_github_decorator():
    open_main_page()
    find_repo('Eva-Shorina/qa_guru_python_3_6')
    go_to_repo()
    open_issues()
    check_issue('1')


@allure.step('Открываем главную страницу github')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Ищем репозиторий {repo}')
def find_repo(repo):
    browser.element('[name=q]').send_keys(repo).press_enter()


@allure.step('Переходим в репозиторий по ссылке')
def go_to_repo():
    browser.element('.repo-list-item a').click()


@allure.step('Открываем таб Issues')
def open_issues():
    browser.element('#issues-tab').double_click()


@allure.step('Проверяем наличие Issue с номером {number}')
def check_issue(number):
    browser.element(by.partial_text('#' + number)).should(be.visible)