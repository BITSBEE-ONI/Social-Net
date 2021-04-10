#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="/home/oni/Music/project01/drivers/chromedriver")

# TEST 0 : Maximize the window
driver.maximize_window()

# TEST 1 : Hit the home page
driver.get("http://127.0.0.1:8000/")
print(driver.current_url)
time.sleep(3)

# TEST 2 : Home page title
print(driver.title)

# TEST 3 : Back and forwarding url from the current url
driver.get("https://www.google.com/")
print(driver.current_url)
driver.back()
print(driver.current_url)
driver.forward()
print(driver.current_url)
driver.back()

# TEST 4 : Sign Up
'''driver.find_element_by_name("firstname").send_keys("Anisul")
driver.find_element_by_name("lastname").send_keys("Islam")
driver.find_element_by_id("username").send_keys("Bitsbee")
driver.find_element_by_name("email").send_keys("anisulislam@gmail.com")

# Does not interactable
driver.find_element_by_name("password").send_keys("SimplePassword")
driver.find_element_by_name("confpassword").send_keys("SimplePassword")


driver.find_element_by_xpath("//*[text()='Sign Up']").send_keys(Keys.ENTER)'''

# TEST 5 : Sign In

driver.find_element_by_class_name("btn-outline-primary").send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_id("email").send_keys("omg")
driver.find_element_by_id("password").send_keys("omg12345")
driver.find_element_by_class_name("btn-primary").send_keys(Keys.ENTER)

time.sleep(5)
print(driver.current_url)
alr = driver.find_element_by_name("mesg")
print(alr.text)

# TEST 6 : Post
driver.find_element_by_xpath("//*[test()='Post']").send_keys(Keys.ENTER)
driver.find_element_by_id("image").send_keys("/home/oni/Music/project01/oni.jpg")
driver.find_element_by_id("captions").send_key("This is the description of the post")
driver.find_element_by_xpath("//*test()='Let\'s Show'").send_keys(Keys.ENTER)

# TEST 8 : Comment
driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/form/textarea").send_keys("This is comment for post 1")
driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/form/button").send_keys(Keys.ENTER)

# TEST 9 : Hide and Show all comment
# show
driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/button[2]").send_keys(Keys.ENTER)
time.sleep(5)
# hide
driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/button[2]").send_keys(Keys.ENTER)

# TEST 10 : Like or Dislike post
# like
driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/button[1]/a").send_keys(Keys.ENTER)
time.sleep(5)
# dislike
driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/button[1]/a").send_keys(Keys.ENTER)

# TEST 11 : Details view of post
driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/a[1]").send_keys(Keys.ENTER)

# TEST 12 : Delete post
driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/a").send_keys(Keys.ENTER)

# TEST 13 : Change password
driver.find_element_by_xpath("/html/body/nav/div/ul/li[5]/div/a[1]").send_keys(Keys.ENTER)
driver.find_element_by_id("id_old_password").send_keys("omg12345")
driver.find_element_by_id("id_new_password1").send_keys("idontknow159")
driver.find_element_by_id("id_new_password2").send_keys("idontknow159")
driver.find_element_by_xpath("/html/body/form/button").send_keys(Keys.ENTER)

# TEST 14 : Edit profile picture and bio
driver.find_element_by_xpath("/html/body/nav/div/ul/li[2]/a").send_keys(Keys.ENTER)
driver.find_element_by_xpath("/html/body/nav/button[3]").send_keys(Keys.ENTER)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/form/input[2]").send_keys("This is ma bio")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/form/input[3]").send_keys("/home/oni/Music/project01/oni.jpg")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/form/button[2]").send_keys(Keys.ENTER)

# TEST 15 : Sign Out

driver.find_element_by_xpath("//*[text()='Sign Out']").send_keys(Keys.ENTER)
alr = driver.find_element_by_name("mesg")
print(alr.text)

time.sleep(5)
# TEST 16 : Unsuccessfull Sign In

driver.find_element_by_class_name("btn-outline-primary").send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_id("email").send_keys("hackerX")
driver.find_element_by_id("password").send_keys("hackerXtream")
driver.find_element_by_class_name("btn-primary").send_keys(Keys.ENTER)

time.sleep(5)
print(driver.current_url)
alr = driver.find_element_by_name("mesg")
print(alr.text)


#driver.close()
print("Test has been run successfully")
