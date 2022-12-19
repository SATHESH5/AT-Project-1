# This file consists of Test Information like username, password, XPATH etc

#TC_login_01

# Python Class for Username and Password
class Sathesh_Data:
    username = "Admin"
    password = "admin123"
    FirstName = "Guvi"
    LastName = "Sathesh"
    

# Python Class for Selenium Selectors
class Sathesh_Selectors:
    input_box_username = "username"
    input_box_password = "password"
    login_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    menu_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/button'
    PIM_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    add_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    input_box_FirstName = "firstName"
    input_box_LastName = "lastName"
    submit_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    
    