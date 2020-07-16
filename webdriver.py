import requests
from selenium import webdriver


driver = webdriver.Chrome(port=7000)
url = 'http://www.baidu.com'
# driver.get(url)
# self.execute(Command.GET, {'url': url})
# url接口：Command.GET: ('POST', '/session/$sessionId/url'),
server_url = 'http://localhost:7000/session/{}/url'.format(driver.session_id)
res = requests.post(server_url, json={'url': url})


