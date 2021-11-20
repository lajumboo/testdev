# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.page.base_page import BasePage


class AddMemberPage(BasePage):
    # 接收driver，并指定类型为WebDriver，用于IDE联想
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    # 添加联系人
    def add_member(self, username, account, phone):
        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return True

    # 验证添加联系人
    def get_member(self):
        member_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        # print(member_list)
        # 获取title属性
        title_list = [element.get_attribute("title") for element in member_list]
        print(title_list)
        # title_list = []
        # for element in member_list:
        #     title_list.append(element.get_attribute("title"))
        return title_list
