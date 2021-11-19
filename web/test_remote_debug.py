# -*- coding: utf-8 -*-
import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestRemoteDebug:
    def setup_method(self):
        # 复用浏览器设置
        # options = Options()
        # options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    # 浏览器复用测试
    def test_remote_debug(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.ID, "menu_contacts").click()

    def test_cookie(self):
        # get_cookies() 可以获取当前打开页面的cookies
        # add_cookie() 可以把cookie添加到当前的页面中

        # cookies = self.driver.get_cookies()
        # print(cookies)

        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'sDLL1VUP7ALjjJwam54Y9aYiWOAdZZZew0x3sNlvFN0ca-NxoNwK5RFxzZla2F30Wqqp_lRIsBrhh_ZPts9u3mE3MdkLZ2sCJMnYr8bq_3eCjLRlCGh2ApL5f-f0H_5jEDflWqDk-7ymoqZE6f331_U8Yxw6nT_4AoKCD-bHhl-NG7drsx5pcCb09kFvIzHkNmX-mTMkwVgOoAmcPPD4cg-AEopybWT1DlMwExq8xYmI1Yv-VoEkTH0TBjWUYX2Nd1lNvhXKjcqcdCR2E7Vg0A'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a6313832'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853388147485'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325116136258'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853388147485'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'secure': False,
             'value': 'true'},
            {'domain': '.qq.com', 'expiry': 1637392747, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1115043491.1637285675'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': True, 'value': '1637285674'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1639898351, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1668821674, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True, 'value': '1637285674'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': True,
             'value': '02069154'},
            {'domain': '.qq.com', 'expiry': 1700378347, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1634916017.1637285675'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': True,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'Cfi1ts_-Scl5TC4egmTyWBJ92IEMZ_JFylVyrnFNOrfmxuZMM0j1JOwSrd-c5G2Y'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': True,
             'value': ''},
            {'domain': '.work.weixin.qq.com', 'expiry': 1668821671, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': True, 'value': '0'}]

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            if 'expiry' in cookie:
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        sleep(5)

    def test_shelve(self):
        # shelve python 内置模块，专门用来进行数据持久化存储，相当于小型的数据库
        # 可以通过 key，value 把数据保存到shelve中

        # # 存储cookie
        # db = shelve.open("cookies")
        # db['cookie'] = cookies
        # db.close()

        # 读取cookie
        db = shelve.open("cookies")
        cookies = db['cookie']
        db.close()

        # 利用读取的cookie 完成登录操作
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()

        # 找到"导入联系人"按钮
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 上传
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
            "D:/hogwarts/web/contacts.xlsx")
        # 验证 上传文件名
        filename = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text

        assert "contacts.xlsx" == filename
        sleep(5)
