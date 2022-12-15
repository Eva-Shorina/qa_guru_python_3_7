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
def test_github():
    browser.open("https://github.com")
    browser.element('[name=q]').send_keys('Eva-Shorina/qa_guru_python_3_6').press_enter()
    browser.element('.repo-list-item a').click()
    browser.element('#issues-tab').double_click()
    browser.element(by.partial_text('#1')).should(be.visible)