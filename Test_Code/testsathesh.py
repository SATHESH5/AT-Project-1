from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import data
import pytest
import time

class Test_Sathesh:
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.close()
        
        def test_login(self, booting_function):
            self.driver.get(self.url)
            time.sleep(5)
            self.driver.find_element(by=By.NAME, value=data.Sathesh_Selectors.input_box_username).send_keys(data.Sathesh_Data.username)
            self.driver.find_element(by=By.NAME, value=data.Sathesh_Selectors.input_box_password).send_keys(data.Sathesh_Data.password)
            self.driver.find_element(by=By.XPATH, value=data.Sathesh_Selectors.login_xpath).click()
            assert self.driver.title == 'OrangeHRM'
            print("The user is logged in successfully")
            
            

            
            
            
            
            
        
        
        