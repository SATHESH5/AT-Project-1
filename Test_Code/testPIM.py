from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import dataPIM
import pytest
import time

class Test_Sathesh:
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.close()
        
        def test_PIM(self, booting_function):
            self.driver.get(self.url)
            time.sleep(5)
            self.driver.find_element(by=By.NAME, value=dataPIM.Sathesh_Selectors.input_box_username).send_keys(dataPIM.Sathesh_Data.username)
            self.driver.find_element(by=By.NAME, value=dataPIM.Sathesh_Selectors.input_box_password).send_keys(dataPIM.Sathesh_Data.password)
            self.driver.find_element(by=By.XPATH, value=dataPIM.Sathesh_Selectors.login_xpath).click()
            time.sleep(3)
            self.driver.find_element(by=By.XPATH, value=dataPIM.Sathesh_Selectors.menu_button).click()
            time.sleep(3)
            self.driver.find_element(by=By.XPATH, Value=dataPIM.Sathesh_Selectors.PIM_item).click()
            time.sleep(3)
            self.driver.find_element(by=By.XPATH, Value=dataPIM.Sathesh_Selectors.add_button).click()
            time.sleep(3)
            self.driver.find_element(by=By.NAME, Value=dataPIM.Sathesh_Selectors.input_box_FirstName).send_keys(dataPIM.Sathesh_Data.FirstName)
            self.driver.find_element(by=By.NAME, Value=dataPIM.Sathesh_Selectors.input_box_LastName).send_keys(dataPIM.Sathesh_Data.LastName)
            self.driver.find_element(by=By.XPATH, value=dataPIM.Sathesh_Selectors.submit_xpath).click()
            assert self.driver.title == 'OrangeHRM'
            print("The user should be able to add a new employee in the PIM and should see a message for successful employee addition")
            
            
            
            
            