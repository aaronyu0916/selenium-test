import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

try:
    driver = webdriver.Chrome() # 啟動 chromedriver
    driver.set_window_size(414,736) #視窗開成iPhonePlus尺寸
    #driver.maximize_window() #視窗最大化
    wait = WebDriverWait(driver, 20)  # 設定等待變數
    driver.get('http://hy-web2-dev.paradise-soft.com.tw/m') # 前往 Dev環境
    wait.until(EC.visibility_of_element_located((By.ID, "nav_btn"))).click() # click右側選單
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "登入"))).click() # click登入頁
    account = driver.find_element_by_id("login-username") # 取得account輸入框
    account.clear()
    account.send_keys('test1111') # 在account內輸入 帳號
    password = driver.find_element_by_id("login-password") # 取得password輸入框
    password.clear()
    password.send_keys('test1111') # 在password輸入 密碼
    login = driver.find_element_by_id("login-button")
    login.click() # 令 chrome driver 按下 點選登入
    #driver.execute_script('window.scrollTo(1000, document.body.scrollHeight);')  # 頁面滾到最下方
    wait.until(EC.visibility_of_element_located((By.XPATH, "//dl/a[@href='/m/lottery']"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, "nzc-index-cqssc"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='game_time_out' and contains(@style,'none')]")))  # 確認頁面未在封盤中才執行下一步
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "game_title")))
    driver.find_element_by_tag_name('h1').click() #找到下注种类：万的分類
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='lm']/div[2]/div/div/table/tbody[2]/tr[1]/td[3]/input")))
    cqssc_bet_input = driver.find_element_by_xpath("//*[@id='lm']/div[2]/div/div/table/tbody[2]/tr[1]/td[3]/input") #取得下注金額輸入框
    cqssc_bet_input.clear() # 清除下注輸入框
    cqssc_bet_input.send_keys('1') # 下注1元
    cqssc_bet_add =  driver.find_element_by_id("game_submit") #找到添加按鈕
    cqssc_bet_add.click() #添加此次下注
    element = wait.until(EC.visibility_of_element_located((By.ID, "game_submit")))
    assert "[F盘] 两面 - 万" in driver.page_source #確定注單有被添加
    element = wait.until(EC.visibility_of_element_located((By.ID, "nzc-buybox-submit")))
    cqssc_bet_submit =  driver.find_element_by_id("nzc-buybox-submit") #找到投注按鈕
    cqssc_bet_submit.click() #點擊投注
    element = wait.until(EC.alert_is_present())
    javascriptAlert = Alert(driver) #取得alert視窗
    javascriptAlert.accept()  #取消掉alert視窗
    time.sleep(0.5)
    nav_btn = driver.find_element_by_id('nav_btn') #找到右上的menu
    nav_btn.click()
    element = wait.until(EC.visibility_of_element_located((By.ID, "nzc-menu-order")))
    betting_records = driver.find_element_by_id("nzc-menu-order")#找到投注紀錄
    betting_records.click()
    element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "order_list")))
    time.sleep(0.5)
    assert "重庆时时彩" in driver.page_source
    assert "投注成功" in driver.page_source
    print("OK")

finally:
    driver.quit() # 關閉 chromedriver


