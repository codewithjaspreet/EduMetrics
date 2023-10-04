import csv
import selenium
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chromedriver_path = "/Users/jaspreetSinghSodhi/downloads/chromedriver"
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--start-maximized") 
driver = webdriver.Chrome( options=chrome_options)



def get_courses(url , name, offered_by, ratings, reviews):

    driver.get(url)

    wait = WebDriverWait(driver, 5)

    # search_box  = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='What do you want to learn?']")))
    # search_box.send_keys("Data Science")
    # search_box.send_keys(Keys.ENTER)

    course_name = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='cds-9 css-18msmec cds-10']//li//div[@class='cds-ProductCard-header']//h3")))

    organisation = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='cds-9 css-18msmec cds-10']//li//div[@class='cds-ProductCard-header']//p")))

    course_rating = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='cds-9 css-18msmec cds-10']//li//div[@class='product-reviews css-pn23ng']//p[@class='cds-119 css-11uuo4b cds-121']")))
    
    course_reviews = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='cds-9 css-18msmec cds-10']//li//div[@class='product-reviews css-pn23ng']//p[@class='cds-119 css-dmxkm1 cds-121']")))
    


    for course in course_name:
        name.append(course.text)

    for offer in organisation:
        offered_by.append(offer.text)

    for rate in course_rating:
        ratings.append(rate.text)

    for review in course_reviews:
        reviews.append(review.text)

 

def automate_coursera(base_url, name, offered_by, rating, reviews):

     
    total_pages = 84

    for page in range(1, total_pages + 1):

        url = base_url + str(page)

        get_courses(url , name, offered_by, rating, reviews)

        
    




if __name__ == '__main__':

    base_url = 'https://www.coursera.org/search?query=data+science&page='

    name = []
    offered_by = []
    rating = []
    reviews = []
    automate_coursera(base_url , name, offered_by, rating, reviews)

    while True:
        pass
