from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://example.com')
driver.find_element_by_name('q').send_keys('automation')
driver.find_element_by_name('btnK').click()
