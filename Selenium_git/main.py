def drive(username,password):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    driver = webdriver.Chrome()
    driver.get("https://github.com/login")
    driver.find_element_by_id("login_field").send_keys(str(username))
    driver.find_element_by_id("password").send_keys(str(password))
    driver.find_element_by_name("commit").click()