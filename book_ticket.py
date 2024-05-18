from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from account import *

def book_tickets(from_station, to_station, date):
    # 创建一个Chrome浏览器对象
    browser = webdriver.Chrome()

    # 打开百度网页
    browser.get('https://kyfw.12306.cn/otn/resources/login.html')

    # 创建WebDriver实例
    time.sleep(3)

    # 输入账号
    browser.find_element(By.ID, 'J-userName').send_keys(account)
    time.sleep(3)

    # 输入密码
    browser.find_element(By.CSS_SELECTOR, '#J-password').send_keys(password)

    # 点击登录
    browser.find_element(By.CSS_SELECTOR, '#J-login').click()

    # 点击购票
    browser.find_element(By.CSS_SELECTOR, '#link_for_ticket').click()

    # 输入初始地
    browser.find_element(By.CSS_SELECTOR, '#fromStationText').clear()
    browser.find_element(By.CSS_SELECTOR, '#fromStationText').send_keys(from_station)
    browser.find_element(By.CSS_SELECTOR, '#fromStationText').click()

    # 输入终点地
    browser.find_element(By.CSS_SELECTOR, '#toStationText').clear()
    browser.find_element(By.CSS_SELECTOR, '#toStationText').send_keys(to_station)
    browser.find_element(By.CSS_SELECTOR, '#toStationText').click()

    # 输入日期
    browser.find_element(By.CSS_SELECTOR, '#train_date').clear()
    browser.find_element(By.CSS_SELECTOR, '#train_date').send_keys(date)
    browser.find_element(By.CSS_SELECTOR, '#train_date').click()

    # 点击查询
    browser.find_element(By.CSS_SELECTOR, '#query_ticket').click()

    # 点击预定
    browser.find_element(By.CSS_SELECTOR, '#btn72').click()

    time.sleep(3)

    # 选择乘车人
    passenger_num = 0
    browser.find_element(By.CSS_SELECTOR, f'#normalPassenger_{passenger_num}').click()

    # 提交订单
    browser.find_element(By.CSS_SELECTOR, '#submitOrder_id').click()
    time.sleep(3)

    # 选择座位
    seat = 'F'
    browser.find_element(By.CSS_SELECTOR, f'#1{seat}').click()
    # 再次确定
    browser.find_element_by_css_selector('#qr_submit_id').click()
    # 关闭浏览器
    browser.quit()