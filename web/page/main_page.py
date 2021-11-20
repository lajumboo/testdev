# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web.page.add_member_page import AddMemberPage
from web.page.base_page import BasePage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame"

    # def __init__(self):
    #     # 跳过登录
    #     options = Options()
    #     options.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome(options=options)

    # 跳转添加联系人页面
    def goto_add_member(self):
        # self.find(By.CSS_SELECTOR, '.index_service_cnt_item').click()
        self.find(By.CSS_SELECTOR, '#menu_contacts').click()
        # self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click(

        locator = (By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)")
        # element: WebElement = WebDriverWait(self.driver, 10).until(
        # expected_conditions.element_to_be_clickable(locator))
        element = self.wait_for_click(locator)
        element.click()

        return AddMemberPage(self.driver)
