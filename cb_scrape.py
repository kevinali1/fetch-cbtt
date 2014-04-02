from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date, datetime
from progressbar import ProgressBar
import urllib2


def fetch_data_categories():
    """
    Fetch the various data categories available from the CBTT
    and output as a dictionary.
    """
    
    url = "http://www.central-bank.org.tt/content/data-centre"
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    all_div_links = soup.find('div', {'class' : 'field-items'} ).findAll('a')
    required_links = [i for i in all_div_links if "http" in i['href']]
    output = {link['href'].split('/')[-1].split('-0')[0]: link['href'] for link in required_links}
    return output



def sync_link_data(verbose=False):
    """
    Fetch the Excel file links corresponding to each data category
    and output as a dictionary.
    """
    
    categories_dict = fetch_data_categories()
    for category, link in categories_dict.items():
        
        # Initialize driver
        print "Initializing Driver"
        driver = webdriver.PhantomJS()
        driver.get(link)
        
        # Click Excel (and deselect html)
        print "Selecting download type"
        driver.find_element_by_id("outputHtml").click()
        driver.find_element_by_id("outputXls").click()
        
        # Set dates
        print "Select start month"
        start_month_select = driver.find_element_by_name('startMonth')
        for option in start_month_select.find_elements_by_tag_name('option'):
            if option.text == 'Jan':
                option.click()
        
        print "Select start year"
        start_year_select = driver.find_element_by_name('startYear')
        for option in start_year_select.find_elements_by_tag_name('option'):
            if option.text == '1991':
                option.click()
        
        print "Select end month"
        end_month_select = driver.find_element_by_name('endMonth')
        for option in end_month_select.find_elements_by_tag_name('option'):
            if option.text == 'Dec':
                option.click()
        
        print "Select end year year"
        end_year_select = driver.find_element_by_name('endYear')
        for option in end_year_select.find_elements_by_tag_name('option'):
            if option.text == '2020':
                option.click()        

        # Click all
        print "Select all fields"
        checkall = driver.find_element_by_id("checkall")
        checkall.click()
        
        #driver.save_screenshot('screen.png') # For testing
        
        # Click submit button
        print "Click submit"
        submitbtn = driver.find_element_by_name("submitBtn")
        submitbtn.click()
        
        # Switch windows
        print "Select new window"
        windows = driver.window_handles
        driver.switch_to_window(windows[-1])
        
        html = driver.page_source
        
