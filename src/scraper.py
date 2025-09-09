# webdriver connects to a given website
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# instantiate web driver, use chrome browser
# mimicks users interaction to opening a web browser
driver = webdriver.Chrome()

# once browser is running, connect to a website (indeed.com for job search) 
driver.get('https://au.indeed.com/jobs?q=&l=Sydney+NSW')

# allow page to load
time.sleep(5)

# inspect element on indeed website, look for class that has the name of the job title
job_titles = driver.find_elements(By.CLASS_NAME, 'jobTitle')
# company name class tag
company_names = driver.find_elements(By.CLASS_NAME, 'css-1h7lukg')
company_locations = driver.find_elements(By.CLASS_NAME, 'css-1restlb')

# use a bunch of classifiers to narrow down url, so need to change classifier
# we look for the h2 class starting with job title
# then we look for the "a" class
company_url = driver.find_elements(By.XPATH, '//h2[starts-with(@class, "jobTitle")]/a')

for title_el, name_el, loc_el, url_el in zip(job_titles, company_names, company_locations, company_url):
    job_title = title_el.text
    company_name = name_el.text
    company_location = loc_el.text
    company_url = url_el.get_attribute('href')

    print("---------------")
    print(f"Job Title: {job_title}")
    print(f"Company: {company_name}")
    print(f"Location: {company_location}")
    print(f"URL: {company_url}")