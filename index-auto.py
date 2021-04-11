#-*- codeing = utf-8 -*-
#@Time : 2021/4/10 14:48
#@Authon : Bin
#@Flie : yiban_auto.py
#@Software : PyCharm

from selenium import webdriver
import time
import os
import webbrowser
import sys


chromfile = os.path.exists('chromedriver.exe')
if (chromfile):
    pass
else:
    print("浏览器驱动不存在，请先安装")
    time.sleep(5)
    sys.exit(0)



print("本程序执行时有15秒等待输入验证码时间，请手动输入验证码")
print(" Copyright © 2021 dibin. All Rights Reserved.")
webbrowser.open_new_tab('https://binfamily.gitee.io/#help')


try:
    wb = webdriver.Chrome("chromedriver.exe")
    wb.implicitly_wait(10)
    wb.get("https://www.yiban.cn/login?go=http%3A%2F%2Fwww.yiban.cn%2F")
    userinfo = input("请输入账号")
    password = input("请输入密码")
    wb.find_element_by_id("account-txt").send_keys(userinfo)
    wb.find_element_by_id("password-txt").send_keys(password)
    kw = wb.find_element_by_id("login-btn")
    kw.click()
    time.sleep(15)   #等待验证码输入
    # kw.click()

    def qiandao():
        #签到模块
        wb.find_element_by_id('tool-sign').click()
        wb.find_element_by_css_selector('span[class="survey-reason"]').click()
        wb.find_element_by_css_selector('.dialog-btn a[class="dialog-confirm"]').click()
        print('签到完成')
    qiandao()
    print("十秒后执行广场模块")
    time.sleep(10)

    def square():
        #账号广场浏览公共群
        pass
      
        print("账号广场执行成功")
    square()
    print("十秒后执行公共群模块")
    time.sleep(10)

    def userinfo():#遍历访问个人主页
      pass
     

    def  qun():
        #公共群
        pass
        print("公共群操作完成")
    qun()
    print("十秒后执行投票模块")
    time.sleep(10)

    def toupiao():
        wb.get("http://www.yiban.cn/my/group")
        pass
        print('投票执行成功')
    toupiao()

    wb.quit()
    print("自动化程序执行完毕")
except Exception as e:
    print(e)
    time.sleep(6)
    wb.quit()
