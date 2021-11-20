# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddMemberPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_member(self):
        username = "张三"
        account = "zhangsan"
        phone = "18600003333"
        sleep(5)
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(account)
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(phone)
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        return True
