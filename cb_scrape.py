from selenium import webdriver

url ="http://www.central-bank.org.tt/content/banking-system-monthly"
driver = webdriver.PhantomJS()
driver.get(url)

# CLick Excel (and deselect html)
driver.find_element_by_id("outputHtml").click()
driver.find_element_by_id("OutputXls").click()

# Click all
checkall = driver.find_element_by_id("checkall")
checkall.click()

# Click submit button
submitbtn = driver.find_element_by_name("submitBtn")
submitbtn.click()

# Switch windows
windows = driver.window_handles
driver.switch_to_window(windows[-1])
