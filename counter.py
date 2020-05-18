from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = "C:\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

def StudentsCounter(class_name):
    Students = []

    #to get the number of all the elements that are classed with the name specified
    number = len(driver.find_elements_by_class_name(class_name))

    #to get the elements text that are classed with the name specified
    for element in driver.find_elements_by_class_name(class_name):    
        Students.append(element.text)
        

    print(f"There are {number} students in {driver.title}")
    print("Names are: ")

    for i in range(number): 
        print(f"{i + 1} - {Students[i]}", sep = "\n")
        
StudentsCounter('y4ihN')