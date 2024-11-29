from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
try: 
        wait = WebDriverWait(driver, 10)
        driver.get('https://test-qa.inlaze.com/auth/sign-in')
        
        email = wait.until(EC.presence_of_element_located(
              (By.CSS_SELECTOR, 'input[id="email"]')
        ))
        email.send_keys('gm@gmail.com')
           
        password = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'input[id="password"]')
        ))
        password.send_keys('Gb12345678@')

        WebDriverWait(driver, 10)
        
        driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

        h2_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
            (By.XPATH, "//h2[@class='font-bold' and text()='g m']")
            )
        )
      
        print(h2_element.text)

        actual_text = h2_element.text.strip().lower()
        expected_text = "g m1"
                
        assert actual_text == expected_text





finally: 
    driver.quit()