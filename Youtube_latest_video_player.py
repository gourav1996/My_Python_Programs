from selenium import webdriver
from selenium.webdriver.common.keys import Keys
name=input("Enter Youtube Channel Name::")
driver = webdriver.Firefox()
driver.get("https://www.youtube.com/c/"+name+"/videos")
element = driver.find_element_by_xpath("//div[1]/div[@id='details' and @class='style-scope ytd-grid-video-renderer' and 1]")
element.click()
quit()

