# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TesterHome:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_sele(self):
        self.driver.get("http://testerhome.com/")
        self.driver.find_element(By.XPATH, '//*[@id="main-nav-menu"]/li[3]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="hot_teams"]//*[@data-name="求职面试圈"]').click()
        time.sleep(5)

    # frame切换
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_id("droppable").text)

        self.driver.switch_to.parent_frame()
        print(self.driver.find_element_by_id("submitBTN").text)
        time.sleep(5)

    # 窗口切换
    def test_windows(self):
        self.driver.get("http://www.baidu.com")
        # 获得百度搜索窗口句柄
        sreach_windows = self.driver.current_window_handle
        print(sreach_windows)
        self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_link_text("立即注册").click()
        # 获得当前所有打开的窗口的句柄
        all_handles = self.driver.window_handles
        print(all_handles)
        # 切换到注册窗口
        for handle in all_handles:
            if handle != sreach_windows:
                self.driver.switch_to.window(handle)
                print('切换到注册窗口')
                self.driver.find_element_by_name("userName").send_keys('username')
                self.driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys('password')
                time.sleep(5)
