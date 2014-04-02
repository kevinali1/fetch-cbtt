from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date, datetime
import urllib2
import time


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



def fetch_download_links(verbose=False):
    """
    Fetch the Excel file links corresponding to each data category
    and output as a dictionary.
    """
    
    output = {}
    categories_dict = fetch_data_categories()
    counter = 0
    num_items = len(categories_dict.items())
    
    for category, link in categories_dict.items():
        
        # Print some progress stats
        print "\n\n\n"
        counter += 1
        print "Fetching item %s of %s" % (str(counter), str(num_items))
        print "Working on %s" % (str(category))
        
        # Initialize driver
        print "Initializing Driver"
        driver = webdriver.PhantomJS()
        driver.get(link)
        
        # Click Excel (and deselect html)
        print "Selecting download type"
        driver.find_element_by_id("outputHtml").click()
        driver.find_element_by_id("outputXls").click()
        
        # Set dates
        #print "Select start month"
        #start_month_select = driver.find_element_by_name('startMonth')
        #for option in start_month_select.find_elements_by_tag_name('option'):
            #if option.text == 'Jan':
                #option.click()
        
        print "Select start year"
        start_year_select = driver.find_element_by_name('startYear')
        for option in start_year_select.find_elements_by_tag_name('option'):
            if option.text == '1991':
                option.click()
        
        #print "Select end month"
        #end_month_select = driver.find_element_by_name('endMonth')
        #for option in end_month_select.find_elements_by_tag_name('option'):
            #if option.text == 'Dec':
                #option.click()
        
        print "Select end year year"
        end_year_select = driver.find_element_by_name('endYear')
        for option in end_year_select.find_elements_by_tag_name('option'):
            if option.text == '2020':
                option.click()        

        # Click all
        print "Select all fields"
        checkall = driver.find_element_by_id("checkall")
        try:
            checkall.click()
        except:
            checkall.send_keys('/n')
        
        # Click submit button
        print "Click submit"
        submitbtn = driver.find_element_by_name("submitBtn")
        try:
            submitbtn.click()
        except:
            submitbtn.send_keys('/n')
        
        # Switch windows
        print "Select new window"
        windows = driver.window_handles
        driver.switch_to_window(windows[-1])
        
        # Get download link
        html = driver.page_source
        soup = BeautifulSoup(html)
        all_links = soup.findAll('a')
        try:
            download_link = [i for i in all_links if "xls" in i['href']]
        except IndexError:
            download_link = None
        
        output.update({category : [link, download_link]})
        
        time.sleep(5)  # Give the api a courtesy rest
        
    return output


def fetch_excel_file(url):
    """
    Given a url for an Excel file, get the file.
    """
    
    response = urllib2.urlopen(url)
    excel_file = 
    


        
        
