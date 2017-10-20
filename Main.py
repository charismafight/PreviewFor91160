# import ghost as g
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import urllib.request
from selenium.webdriver.common.keys import Keys
from PIL import Image
import pytesseract
import io

login_url = "https://user.91160.com/login.html"
browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browser.get(login_url)
time.sleep(2)
username = browser.find_element_by_name("username")
username.send_keys("17771819183")
password = browser.find_element_by_name("password")
password.send_keys("7u82enpa")
loginUser = browser.find_element_by_name("loginUser")
loginUser.click()
time.sleep(2)


def element_exists_by_class_name(class_name):
    a = None
    try:
        a = browser.find_element_by_class_name(class_name)
    except NoSuchElementException:
        return a
    return a


def element_exists_by_link_text(text):
    a = None
    try:
        a = browser.find_elements_by_link_text(text)
    except NoSuchElementException:
        return a
    return a


def element_exists_by_id(id):
    a = None
    try:
        a = browser.find_element_by_id(id)
    except NoSuchElementException:
        return a
    return a


count = 1
while 1 == 1:
    print('count:', count)
    count += 1
    # 钟宇玲测试用
    # browser.get('https://www.91160.com/doctors/index/unit_id-105/dep_id-2791/docid-20795.html')
    # 朱素君
    browser.get("https://www.91160.com/doctors/index/unit_id-105/dep_id-2791/docid-20860.html")
    time.sleep(0.3)

    appointment = element_exists_by_class_name('orderLogin')
    if appointment:
        appointment.click()
        time.sleep(0.3)
        # time
        time_ul = element_exists_by_id('delts')
        time_ul.find_element_by_tag_name('li').click()
        # person set default person can ignore this step
        # radio_button = browser.find_element_by_name('mid')
        # radio_button.click()
        # rule checkbox
        check_box = element_exists_by_id('check_yuyue_rule')
        check_box.click()
        # # todo 验证码需要先点击一次，否则页面不会有真实的url
        # element_exists_by_id('vertifyCodeImg').click()
        # time.sleep(0.1)
        # img_url = element_exists_by_id('vertifyCodeImg').get_attribute('src')
        # print('imgurl:' + img_url)
        # fd = urllib.request.urlopen(img_url)
        # img_file = io.BytesIO(fd.read())
        # img = Image.open(img_file)
        # print(pytesseract.image_to_string(img))
        # submit = element_exists_by_id('submitbtn')
        # submit.click()
        # print('submited')
        exit(0)
