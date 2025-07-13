from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Setup
driver = webdriver.Chrome()
driver.get("http://localhost:3000/")
driver.maximize_window()
time.sleep(5)

# Click Register Link
register_link = driver.find_element(By.XPATH, "//a[text()='Register']")
register_link.click()
time.sleep(4)

# Fill the form fields
driver.find_element(By.ID, "register-name").send_keys("Tosin Williams")
driver.find_element(By.ID, "register-email").send_keys("tosinqa@gmail.com")
driver.find_element(By.ID, "register-password").send_keys("TestPassword123")
time.sleep(3)

# Click Register Button
register_button = driver.find_element(By.CSS_SELECTOR, ".register-btn")
register_button.click()
time.sleep(5)

# Click on 'Schedule Pickup'
schedule_pickup_btn = driver.find_element(By.XPATH, "/html/body/div/div/nav/div/div/a[2]")
schedule_pickup_btn.click()
time.sleep(4)

# Fill Schedule Pickup Form
driver.find_element(By.ID, "home-name").send_keys("Tosin A. Williams")
driver.find_element(By.ID, "home-email").send_keys("tosinqa@gmail.com")
time.sleep(2)

pickup_location = Select(driver.find_element(By.ID, "home-location"))
pickup_location.select_by_visible_text("Nairobi")
time.sleep(2)

waste_type_dropdown = Select(driver.find_element(By.ID, "home-waste"))
waste_type_dropdown.select_by_visible_text("General Waste")
time.sleep(2)

driver.find_element(By.ID, "home-date").send_keys("07-15-2025")
driver.find_element(By.ID, "home-desc").send_keys("3 bins of plastic waste ready for pickup.")
time.sleep(2)

# Submit pickup request
submit_btn = driver.find_element(By.CLASS_NAME, "home-btn")
submit_btn.click()
time.sleep(5)

# Navigate to Login
login_link = driver.find_element(By.XPATH, "/html/body/div/div/nav/div/div/a[8]")
login_link.click()
time.sleep(4)

# Login
driver.find_element(By.ID, "login-email").send_keys("tosinqa@gmail.com")
driver.find_element(By.ID, "login-password").send_keys("TestPassword123")
time.sleep(2)

login_button = driver.find_element(By.CSS_SELECTOR, ".login-btn")
login_button.click()
time.sleep(5)

# Dashboard
dashboard_link = driver.find_element(By.XPATH, "/html/body/div/div/nav/div/div/a[3]")
dashboard_link.click()
time.sleep(5)

# Blog
blog_link = driver.find_element(By.XPATH, "/html/body/div/div/nav/div/div/a[4]")
blog_link.click()
time.sleep(5)

# Community
community_link = driver.find_element(By.XPATH, "/html/body/div/div/nav/div/div/a[5]")
community_link.click()
time.sleep(5)

# Awareness
awareness_link = driver.find_element(By.XPATH, "/html/body/div/div/nav/div/div/a[6]")
awareness_link.click()
time.sleep(5)

# Feedback
feedback_link = driver.find_element(By.XPATH, "/html/body/div/div/nav/div/div/a[7]")
feedback_link.click()
time.sleep(5)

# Logout
logout_button = driver.find_element(By.CLASS_NAME, "nav-logout")
logout_button.click()
time.sleep(4)

# Close browser
driver.quit()


