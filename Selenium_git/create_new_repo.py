def createrepo(username,password,reponame,visibility,readme,desc):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from main import drive
    #repo_name -> name of the repo
    #visibility -> public(1) or private(0)
    #readme
    #desc ->description

    driver = webdriver.Chrome()
    driver.get("https://github.com/login")
    driver.find_element_by_id("login_field").send_keys(str(username))
    driver.find_element_by_id("password").send_keys(str(password))
    driver.find_element_by_name("commit").click()
    #driver.get("https://github.com/login")
    #drive("","h")
    driver.find_element_by_xpath("//a[@class = 'btn btn-sm btn-primary text-white']").click()
    driver.find_element_by_xpath("//input[@name='repository[name]']").send_keys(reponame)
    driver.find_element_by_xpath("//input[@name='repository[description]']").send_keys(desc)
    if(int(visibility) == 1): #public
        driver.find_element_by_xpath("//input[@name='repository[visibility]' and @id = 'repository_visibility_public']").click()
    elif(int(visibility) == 0): #private
        driver.find_element_by_xpath("//input[@name='repository[visibility]' and @id = 'repository_visibility_private']").click()
    driver.find_element_by_xpath("//input[@name='repository[auto_init]' and @id = 'repository_auto_init']").click()
    driver.find_element_by_xpath('//button[@type="submit" and @data-disable-with="Creating repository…"]').click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//button[@type="submit" and @data-disable-with="Creating repository…"]'))).click()

    
createrepo("","","heyy",1,"d","jk")