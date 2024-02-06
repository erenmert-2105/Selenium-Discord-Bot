import time
import gırısb
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def Run():
    a = 0
    b = 0
    list()
    driver = webdriver.Chrome()

    driver.get("https://discord.com/login")
    time.sleep(3)
    # ıd and password in grısb
    # **********************************
    username = driver.find_element_by_xpath(
        "//*[@id='app-mount']/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input")
    password = driver.find_element_by_xpath(
        "//*[@id='app-mount']/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input")
    username.send_keys(gırısb.id)
    password.send_keys(gırısb.password)
    login_button = driver.find_element_by_xpath(
        "//*[@id='app-mount']/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]")
    login_button.click()
    # ***********************************
    time.sleep(10)
    # channel url
    driver.get("https://discord.com/channels/738028076650201239/738028076650201242")
    time.sleep(5)
    # chat adress
    elements = driver.find_elements_by_css_selector(".markup-2BOw-j.messageContent-2qWWxC")
    for element in elements:
        a = a + 1
    while True:
        if b == 1:
            break
        while True:
            elements = driver.find_elements_by_css_selector(".markup-2BOw-j.messageContent-2qWWxC")
            try:
                elements[a]
                break
            except:
                # time.sleep(0.1) if your pc lagged
                pass

        kelimelerim = (elements[a].text).split()
        sade_k = list()
        for i in kelimelerim:
            # filters
            i = i.strip("\n")
            i = i.strip(",")
            i = i.strip(" ")
            i = i.strip(":")
            sade_k.append(i)
        # researched key word
        for i in sade_k:
            if (i) == ("tank"):
                b = 1
                break
            else:
                a = a + 1

    msg_input = driver.find_element_by_xpath(
        '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div[2]/div')
    # delay here if wanted time.sleep(x)
    # answer
    msg_input.send_keys("bot düzgün çalışıyor")
    msg_input.send_keys(Keys.ENTER)
    onay=input(print("devam etmek istiyormusun evet(1) hayır(2)"))
    if onay == ("1"):
        Run()
    else:
        driver.close()
Run()


