from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Capstone1.Test_Data import data
from Capstone1.Test_Locator import locators
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class Test_Project:
# Boot method to run Pytest using POM
   @pytest.fixture
   def setup(self):
      # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="114.0.5735.90").install()))
      service = Service(executable_path="C:\\Users\\NANDHU\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe")
      self.driver = webdriver.Firefox(service=service)
      self.driver.maximize_window()
      self.wait = WebDriverWait(self.driver, 20)
      self.action =ActionChains(self.driver)
      yield
      self.driver.close()
 # Testcase 1:login testing with valid password (TC_Login_01)
   def test_login_valid_credential(self,setup):
       self.driver.get(data.Data().url)
       try:
           cookie_before = self.driver.get_cookies()[0]['value']
           username_field = self.wait.until(EC.presence_of_element_located((By.NAME, locators.Login().username_text_box)))
           username_field.send_keys(data.Data().username)

           pswrd_field = self.wait.until(EC.presence_of_element_located((By.NAME, locators.Login().password_text_box)))
           pswrd_field.send_keys(data.Data().valid_password)

           button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators.Login().login_btn)))
           button.click()
           cookie_after = self.driver.get_cookies()[0]['value']
           assert cookie_before != cookie_after
           print("LOGIN SUCCESS WITH VALID PASSWORD")
       except TimeoutException as e:
           print(e)


# Testcase 2 :login testing with invalid password (TC_Login_02)

   def test_login_invalid_credential(self,setup):
        self.driver.get(data.Data().url)
        try:
           cookie_before = self.driver.get_cookies()[0]['value']
           username_field = self.wait.until(EC.presence_of_element_located((By.NAME, locators.Login().username_text_box)))
           username_field.send_keys(data.Data().username)

           pswrd_field = self.wait.until(EC.presence_of_element_located((By.NAME, locators.Login().password_text_box)))
           pswrd_field.send_keys(data.Data().invalid_password)

           button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators.Login().login_btn)))
           button.click()
           cookie_after = self.driver.get_cookies()[0]['value']
           assert cookie_before == cookie_after
           print("LOGIN FAILED WITH INVALID PASSWORD")
        except TimeoutException as e:
            print(e)
# Test case:3 Adding a New Employee in Pim Module TC_PIM_01
   def test_Pim_module(self,setup):

       self.driver.get(data.Data().url)
       try:
           username_field = self.wait.until(EC.presence_of_element_located((By.NAME, locators.Login().username_text_box)))
           username_field.send_keys(data.Data().username)

           pswrd_field = self.wait.until(EC.presence_of_element_located((By.NAME, locators.Login().password_text_box)))
           pswrd_field.send_keys(data.Data().valid_password)

           button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators.Login().login_btn)))
           button.click()
           # Navigate to Pim tab
           pim_module = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pim_module.pim_menu)))
           pim_module.click()

        # Adding New Employee
           add_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pim_module.add_btn)))
           add_btn.click()
           firstname = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Pim_module.first_name)))
           firstname.send_keys(data.Pim().first_Name)
           mid_name = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Pim_module.mid_name)))
           mid_name.send_keys(data.Pim().mid_Name)
           lname = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Pim_module.last_name)))
           lname.send_keys(data.Pim().last_Name)
           save_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pim_module().save_btn)))
           save_btn.click()
           employee_list = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Pim_module().emply_list)))
           assert employee_list.is_displayed()
           print("New Employee Added Successfully")

   # Adding Personal information of the New Employee

           nick_name = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Pim_module().nick_name)))
           nick_name.send_keys(data.Pim().nick_name)
           other_id = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Pim_module().other_id)))
           other_id.send_keys(data.Pim().other_id)
           license_num = self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Pim_module().License_Number)))
           license_num.send_keys(data.Pim().License_number)
           Expiry_Date = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Pim_module().Expiry_Date)))
           Expiry_Date.send_keys(data.Pim().Expiry_Date)
           SSN_number = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Pim_module().SSN_number)))
           SSN_number.send_keys(data.Pim().SSN_number)
           SIN_number = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Pim_module().SIN_number)))
           SIN_number.send_keys(data.Pim().SIN_number)
           date = self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Pim_module().Date_birth)))
           date.send_keys(data.Pim().Data_birth)
           Nation = self.wait.until(EC.element_to_be_clickable((By.XPATH,locators.Pim_module().nationality_drop)))
           self.action.click(on_element=Nation)
           self.action.perform()
           drop = self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Pim_module().drop_down_select)))
           self.action.click(on_element=drop)
           self.action.perform()

           smoker_checkbox = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pim_module().smoker_checkbox)))
           smoker_checkbox.click()
           service_box = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Pim_module().service_box)))
           service_box.send_keys(data.Pim().service)
           gender = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pim_module().gender)))
           gender.click()
           save_new = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pim_module().save_button)))
           save_new.click()
           employee_list = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Pim_module().emply_list)))
           assert employee_list.is_displayed()
           print("New Employee personal details added Successfully!!")
       except TimeoutException or NoSuchElementException as e:
           print(e)

# Test case:4 Edit the Existing Employee TC_PIM_02
   def test_Edit_module(self,setup):

       self.driver.get(data.Data().url)
       try:
           #Edit the Existing employee
           username_field = self.wait.until(EC.presence_of_element_located((By.NAME, locators.Login().username_text_box)))
           username_field.send_keys(data.Data().username)

           pswrd_field = self.wait.until(EC.presence_of_element_located((By.NAME, locators.Login().password_text_box)))
           pswrd_field.send_keys(data.Data().valid_password)

           button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators.Login().login_btn)))
           button.click()
           # Navigate to Pim tab
           pim_module = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pim_module.pim_menu)))
           pim_module.click()

           # search existing employee name and id

           firstname = self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Pim_module().firstname)))
           firstname.send_keys(data.Pim().first_Name)
           employee_id = self.driver.find_element(By.XPATH,locators.Pim_module().employee_id)
           employee_id.send_keys(data.Pim().employee_id)
           search = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pim_module().search_btn)))
           search.click()
           edit=self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pim_module().edit_btn)))
           edit.click()

           # Edit the Exisiting Employee Personal Details
           nick = self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Pim_module().nick_name)))
           nick.send_keys(5 * Keys.BACKSPACE)
           nick.send_keys(data.Pim().nick)
           save = self.wait.until(EC.element_to_be_clickable((By.XPATH,locators.Pim_module().save_button1)))
           save.click()
           employee_list = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Pim_module().emply_list)))
           assert employee_list.is_displayed()
           print("Personal details edited Successfully!!")

       except TimeoutException as e:
           print(e)

# Test case:5 Delete the Existing Employee TC_PIM_03
   def test_delete_module(self, setup):
       self.driver.get(data.Data().url)
       try:
          username_field = self.wait.until(EC.presence_of_element_located((By.NAME, locators.Login().username_text_box)))
          username_field.send_keys(data.Data().username)

          pswrd_field = self.wait.until(EC.presence_of_element_located((By.NAME, locators.Login().password_text_box)))
          pswrd_field.send_keys(data.Data().valid_password)

          button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators.Login().login_btn)))
          button.click()
       # Navigate to Pim tab
          pim_module = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pim_module.pim_menu)))
          pim_module.click()

       # search existing employee name and id

          firstname = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Pim_module().firstname)))
          firstname.send_keys(data.Pim().first_Name)
          employee_id = self.driver.find_element(By.XPATH, locators.Pim_module().employee_id)
          employee_id.send_keys(data.Pim().employee_id1)
          search = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pim_module().search_btn)))
          search.click()

       # Delete Existing employee

          delete = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pim_module().delete_btn)))
          delete.click()
          confirm = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pim_module().confirm_btn)))
          confirm.click()
          employee_list = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Pim_module().emply_list)))
          assert employee_list.is_displayed()
          print("Existing employee deleted Successfully!!")

       except TimeoutException as e:
         print(e)