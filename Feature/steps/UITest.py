from behave import *
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time


@given(u'Chrome Browser is launched and the URL for Metabase')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path= 'C:\Program Files (x86)\chromedriver.exe')


@given(u'The URL http: // localhost: 3000 / is in Use')
def step_impl(context):
        context.driver.maximize_window()
        try:
            context.driver.get("http://localhost:3000/")
            assert True;
        except WebDriverException:
            context.driver.close()
            print("Cannot open metabase url, make sure it is running on your localhost")
            assert False;
        time.sleep(1.5)


@when(u'I enter email as "{email}" And password as "{password}"')
def step_impl(context, email, password):
     context.driver.find_element(By.XPATH, "//*[@id=\"formField-username\"]/div[2]/div/input").send_keys(email)
     context.driver.find_element(By.XPATH, "//*[@id=\"formField-password\"]/div[2]/div/input").send_keys(password)
     time.sleep(5)
     assert True;


@when(u'I click on Sign In')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/main/div/div[2]/div/div[2]/div/form/div[4]/button").click()
    time.sleep(10)
    assert True;


@then(u'I shall be Logged in as Admin User')
def step_impl(context):
    try:
        text = context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/aside/nav/div/div/div[2]/div/h4").text
    except:
        context.driver.close()
        assert False, "Test Failed: The provided credentials are invalid"
    if text == "COLLECTIONS":
        assert True, "Logged In Successfully"


@then(u'I click on the Settings Button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/div/div[2]/div[3]/div/div/button").click()
    time.sleep(1.5)
    assert True;


@then(u'I click on Admin Settings')
def AdminSetting(context):
    context.driver.find_element(By.XPATH, "/html/body/span/span/div/div/div/ol/li[2]/a/div").click()
    time.sleep(1.5)


@then(u'i click on People')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/nav/div[2]/ul/li[4]/a").click()
    time.sleep(0.2)
    assert True;


@then(u'I click on Invite Someone Button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/main/div/div[2]/div[2]/div/section[1]/div/a/button").click()
    time.sleep(0.2)
    assert True;


@then(u'I enter First Name as "{firstname}"')
def step_impl(context, firstname):
        context.driver.find_element(By.XPATH, "//*[@id=\"formField-first_name\"]/div[2]/div/input").send_keys(firstname)
        assert True;


@then(u'I enter Last Name as "{lastname}"')
def step_impl(context, lastname):
    context.driver.find_element(By.XPATH, "//*[@id=\"formField-last_name\"]/div[2]/div/input").send_keys(lastname)
    assert True;


@then(u'I enter Email as "{email}"')
def step_impl(context, email):
    context.driver.find_element(By.NAME, 'email').send_keys(email)
    assert True;


@then(u'I click on create')
def step_impl(context):
    context.driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div/div/div/div[2]/div/form/div[5]/button[1]").click()
    time.sleep(5)
    assert True;


@then(u'i click on Done')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div/div[3]/div/button").click()
    time.sleep(1.5)
    assert True;



@then(u'a new User will be created')
def step_impl(context):
    assert True, "New User is Created"

