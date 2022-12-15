import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from allure_commons.types import Severity

def test_github_with_steps():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.label('owner', 'eva.shorina')
    allure.dynamic.feature('Issues в репозитории')
    allure.dynamic.story('Проверка номера issue')
    allure.dynamic.link('https://github.com', name='Testing')

    with allure.step('Открываем главную страницу github'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий с домашним заданием'):
        browser.element('[name=q]').send_keys('Eva-Shorina/qa_guru_python_3_6').press_enter()

    with allure.step('Переходим в репозиторий по ссылке'):
        browser.element('.repo-list-item a').click()

    with allure.step('Открываем таб Issues'):
        browser.element('#issues-tab').double_click()

    with allure.step('Проверяем наличие Issue с номером 1'):
        browser.element(by.partial_text('#1')).should(be.visible)