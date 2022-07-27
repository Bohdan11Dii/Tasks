import json
import random
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
# from get_chromedriver import get_chromedriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import re


def my_profile(username, password, hashtag):
    try:
            s = Service('/home/bodya/Документи/Future_Job/Second_task/chromdriver/chromedriver')
            # browser = webdriver.Chrome('chromdriver/chromedriver')
            browser = webdriver.Chrome(service=s)
            # browser = webdriver.Chrome(get_chromedriver())

            browser.get('https://www.instagram.com')
            time.sleep(random.randrange(3, 10))

            username_input = browser.find_element(by=By.NAME, value='username')
            username_input.clear()
            username_input.send_keys(username)

            time.sleep(2)

            password_input = browser.find_element(by=By.NAME, value='password')
            password_input.clear()
            password_input.send_keys(password)

            password_input.send_keys(Keys.ENTER)

            time.sleep(5)

            try:
                browser.get(f'https://www.instagram.com/{hashtag}/')
                time.sleep(5)

                hrefs = browser.find_elements(By.TAG_NAME, 'a')


                # posts_urls = [item.get_attribute('href') for item in hrefs if '/p' in item.get_attribute('href') ]

                posts_urls = []
                for item in hrefs:
                    href = item.get_attribute('href')

                    if "/p" in href:
                        posts_urls.append(href)
                        # print(href)

                # print(posts_urls)

                for url in posts_urls[0:1]:
                    browser.get(url + 'liked_by/')
                    time.sleep(5)

                    soup = BeautifulSoup(browser.page_source, 'lxml')

                    users = soup.find('main', class_='_a993 _a995')

                    users = users.find_all('div', class_='_aacl _aaco _aacw _aacx _aada _ab58')

                    list_of_users = []

                    for i in users:
                        list_of_users.append(i.get_text())

                    # print(list_of_users)
                    data = ''
                    error = False
                    error_message = None
                    # invalid_symbols = r'^[^0-9]'
                    invalid_symbols = [str(n) for n in range(1, 11)]
                    for name in list_of_users:
                        for symbol in name:
                            if symbol in invalid_symbols:
                                error = True
                                error_message = f"The name {name} consists of numbers -- {symbol}. This expression is not applicable"
                                print(error_message)
                                break
                    if error is False and list_of_users == []:
                        data = 'eto nikomy me nravitsa'
                    elif error is False and len(list_of_users) == 2:
                        data = f'{list_of_users[0]} and {list_of_users[1]} liked it'
                    elif error is False and len(list_of_users) == 3:
                        data = f'{list_of_users[0]}, {list_of_users[1]} and {list_of_users[2]} liked it'
                    elif error is False and len(list_of_users) > 3:
                        data = f'{list_of_users[0]}, {list_of_users[1]} and {len(list_of_users) - 2} liked it'
                    Response = [{
                        'data': data,
                        'error': error,
                        'error_message': error_message
                    }]
                    json.dump(Response, open('Response.json', 'w'), ensure_ascii=False, indent=2)

                    return Response

                browser.close()
                browser.quit()

            except Exception as ex:
                print(ex)
                # browser.close()
                # browser.quit()

            browser.close()
            browser.quit()
    except Exception as ex:
            print(ex)
            # browser.close()
            # browser.quit()


users = my_profile(username, password, 'bodya_11dii')
# get_valid(users)