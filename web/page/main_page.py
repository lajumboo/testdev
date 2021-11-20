# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from web.page.add_member_page import AddMemberPage


class MainPage:

    def __init__(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    def goto_add_member(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_item').click()
        return AddMemberPage(self.driver)
