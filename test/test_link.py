# -*- coding: utf-8 -*-
import allure

TEST_CASE_LINK = 'https://docs.qameta.io/allure/'


@allure.title("添加链接")
@allure.testcase(TEST_CASE_LINK, "测试用例链接")
def test_link():
    pass


@allure.title("添加文本")
def test_attach_text():
    allure.attach("这是一个文本", "文本测试", attachment_type=allure.attachment_type.TEXT)


@allure.title("添加HTML")
def test_attach_html():
    allure.attach("<body>这是一段html</body>", "html测试", attachment_type=allure.attachment_type.HTML
                  )


@allure.title("添加图片")
def test_attach_photo():
    allure.attach.file("C:/Users/10505/Pictures/Saved Pictures/692912.JPG", name="这是一个图片",
                       attachment_type=allure.attachment_type.JPG)


@allure.title("添加视频")
def test_attach_video():
    allure.attach.file("C:/Users/10505/Videos/Northern lights.MP4", name="这是一个视频",
                       attachment_type=allure.attachment_type.MP4)
