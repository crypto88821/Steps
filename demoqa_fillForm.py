from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as auto
import random
from behave import *

#====================================================
#BDD Framework
#===================================================

@given('Launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

@when('I go to automation practice form')
def step_impl(context):
    context.driver.get('https://demoqa.com/automation-practice-form')

@when('I fill the First Name and Last Name')
def step_impl(context):
    context.driver.find_element_by_id("firstName").send_keys('TEST')
    context.driver.find_element_by_id("lastName").send_keys('TEST')

@when('I fill the Email')
def step_impl(context):
    context.driver.find_element_by_id("userEmail").send_keys("test@mail.com")

@when('I fill the mobile number')
def step_impl(context):
    context.driver.find_element_by_id("userNumber").send_keys('0866554541')    

@when('I choose gender randomly')
def step_impl(context):
    RandomGender = ["gender-radio-1","gender-radio-2","gender-radio-3"]
    i = random.randrange(0,2)
    radioButton = context.driver.find_element_by_id(RandomGender[i])
    context.driver.execute_script("arguments[0].click();", radioButton) 

@when('I choose DOB randomly')
def step_impl(context):
    #Open DatePicker
    context.driver.find_element_by_id("dateOfBirthInput").click()  

    #selecting Month
    month = context.driver.find_element_by_class_name('react-datepicker__month-select')
    wait(context.driver,10).until(EC.element_to_be_clickable,(month.click()))
    selector = Select(month)
    options = selector.options
    randMonth = random.randrange(0,11)
    for index in range(0,len(options)-1):
        print(options[index].text)
    selector.select_by_index(randMonth)
    wait(context.driver,10).until(EC.element_to_be_clickable,(month.click()))

    #selecting Year  
    year = context.driver.find_element_by_class_name('react-datepicker__year-select')
    wait(context.driver,10).until(EC.element_to_be_clickable,(year.click()))
    selector = Select(year)
    options = selector.options
    RandYear = random.randrange(1970,2000)
    randYear = str(RandYear)
    #for index in range(0,len(options)-1):
    #    print(options[index].text)
    selector.select_by_value(randYear)
    wait(context.driver,10).until(EC.element_to_be_clickable,(year.click()))

    #selecting Day
    day = context.driver.find_element_by_class_name('react-datepicker__week')
    #clicking random day
    wait(context.driver,10).until(EC.element_to_be_clickable,(day.click()))

@when('I pick any subject randomly')
def step_impl(context):
    subjectField = context.driver.find_element_by_id('subjectsContainer')   
    subjectNum = random.randrange(1,5)
    letter = ['a','i','u','e','o']
    #Choosing random subject
    x=0
    while x <= subjectNum:
        subjectField.click()
        i = random.randrange(0,4)
        auto.write((letter[i]))
        auto.press('enter')
        x+=1

@when('I tick any hobbies randomly')
def step_impl(context):
    hobbiesList = [
    '//*[@id="hobbiesWrapper"]/div[2]/div[1]/label',
    '//*[@id="hobbiesWrapper"]/div[2]/div[2]/label',
    '//*[@id="hobbiesWrapper"]/div[2]/div[3]/label']  
    hobbiesNum = random.randrange(1,3)
    x=0
    while x <= hobbiesNum:
        hobby = context.driver.find_element_by_xpath(hobbiesList[x])
        context.driver.execute_script("arguments[0].click();", hobby)
        x+=1 

@when('I upload my profile picture')
def step_impl(context):
    pictureButton = context.driver.find_element_by_id('uploadPicture')
    #scrolling into the element
    context.driver.execute_script('arguments[0].scrollIntoView();',pictureButton)
    #uploading the file
    context.driver.find_element_by_id('uploadPicture').send_keys('C://Users//62852//Pictures//Aselole//Akhmad Noor.jpg')

@when('I type my current address')
def step_impl(context):
    context.driver.find_element_by_id('currentAddress').send_keys('Jl Tanjung no 126 Sorosutan Umbulharjo Yogyakarta')

@when('I choose my State and my City')
def step_impl(context):
    context.driver.find_element_by_id('state').click()
    auto.write('a')
    auto.press('enter')

    context.driver.find_element_by_id('city').click()
    auto.write('a')
    auto.press('enter')


@when('I click Submit button')
def step_impl(context):
    context.driver.find_element_by_id('submit').click()


@then('Verify that')
def step_impl(context):
    context.driver.quit()    
