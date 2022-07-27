# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# def get_chromedriver():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get("https://www.google.com")

import requests

names = requests.body['names']
names = names.split(',')
data = ''
error = False
error_message = None
for name in names:
    for symbol in name:
        if symbol in invalid_symbols:
            error = True
            error_message = 'name {name} contains invalid symbol {symbol}'
            break
if error is False and names == []:
  data = 'eto nikomy me nravitsa'
elif error is False and len(names) == 2:
  data = f'{names[0]} and {names[1]} liked it'
elif error is False and len(names) == 3:
  data = f'{names[0]}, {names[1]} and {names[2]} liked it'
elif error is False abd len(names) > 3:
  data = f'{names[0]}, {names[1]} and {len(names) - 2} liked it'
Response({
    'data': data,
    'error': error,
    'error_message': error_message
})