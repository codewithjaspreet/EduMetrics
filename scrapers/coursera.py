import csv
import selenium
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.helper import make_csv
chromedriver_path = "/Users/jaspreetSinghSodhi/downloads/chromedriver"
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--start-maximized") 
driver = webdriver.Chrome( options=chrome_options)



def get_courses(url , name, offered_by, ratings, reviews, others):

    driver.get(url)

    wait = WebDriverWait(driver, timeout= 15)

    course_name = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='cds-9 css-18msmec cds-10']//li//div[@class='cds-ProductCard-header']//h3")))

    organisation = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='cds-9 css-18msmec cds-10']//li//div[@class='cds-ProductCard-header']//p")))

    course_rating = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='cds-9 css-18msmec cds-10']//li//div[@class='product-reviews css-pn23ng']//p[@class='cds-119 css-11uuo4b cds-121']")))
    
    course_reviews = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='cds-9 css-18msmec cds-10']//li//div[@class='product-reviews css-pn23ng']//p[@class='cds-119 css-dmxkm1 cds-121']")))

    other = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='cds-9 css-18msmec cds-10']//li//div[@class='cds-CommonCard-metadata']//p")))

    for course in course_name:
        name.append(course.text)

    for offer in organisation:
        offered_by.append(offer.text)

    for rate in course_rating:
        ratings.append(rate.text)

    for review in course_reviews:
        reviews.append(review.text)

    for other_info in other:
        others.append(other_info.text)
       


 

def automate_coursera(base_url, name, offered_by, rating, reviews , others):

     
    total_pages = 84

    
    for page in range(1, total_pages + 1):

        print(f"Getting page: {page}")

        url = base_url + str(page)

        get_courses(url , name, offered_by, rating, reviews  , others)

        
    




if __name__ == '__main__':

    base_url = 'https://www.coursera.org/search?query=data+science&page='

    name = []
    offered_by = []
    rating = []
    reviews = []
    others = []
    automate_coursera(base_url , name, offered_by, rating, reviews , others)

    headers = ["Course Name", "Offered By", "Rating", "Reviews" , "Other" ] 

    make_csv("Coursera", headers, name, offered_by, rating, reviews , others)

    while True:
        pass
