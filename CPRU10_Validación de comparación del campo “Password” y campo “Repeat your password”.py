from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
try: 
        wait = WebDriverWait(driver, 10)
        driver.get('https://test-qa.inlaze.com/auth/sign-in')
        form_auth_link = wait.until(EC.presence_of_element_located(
              (By.LINK_TEXT, 'Sign up')
        ))
        form_auth_link.click()

        fullname = wait.until(EC.presence_of_element_located(
              (By.CSS_SELECTOR, 'input[id="full-name"]')
        ))
        fullname.send_keys('Maria Benitez')

        email = wait.until(EC.presence_of_element_located(
              (By.CSS_SELECTOR, 'input[id="email"]')
        ))
        email.send_keys('mariab@gmail.com')
           
        password = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'input[id="password"]')
        ))
        password.send_keys('Gb12345678@ss')
        
        confirmpassword = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'input[id="confirm-password"]')
        ))
        confirmpassword.send_keys('Gb12345678@')
        
        label_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
          (By.XPATH, "//label[@class='label text-error' and contains(text(), 'Passwords do not match')]")
          ) 
        )  


        #actual_text = label_element.text.strip().lower()
        #expected_text = "successful registration!"


        #assert actual_text == expected_text

finally: 
    driver.quit()