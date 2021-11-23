# -*- coding: utf-8 -*-
import time
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestDaka:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["noReset"] = "True"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='工作台']").click()
        # 滚动查找
        sleep(5)
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("打卡").instance(0));').click()
        # settings
        self.driver.update_settings({"waitForIdleTimeout": 0})
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        time.sleep(5)
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()

        # 显式等待
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)
