from selenium import webdriver
import os

print("Functional tests executing...")

cwd = os.getcwd()
print("Current working directory: " + cwd)

path="C:\\programming\\python\\django\\geckodriver.exe"
browser=webdriver.Chrome(path)
browser.get("http://localhost:8000")

assert 'Django' in browser.title
#driver.close()
#driver.quit()