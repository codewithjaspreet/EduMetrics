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



def get_courses(url ,  name, rating, reviews , total_duration,offered_by):

    driver.get(url)


    wait = WebDriverWait(driver, timeout= 15)

    ratings = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='ud-heading-sm star-rating-module--rating-number--2xeHu']")))

    review = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='ud-text-xs course-card-ratings-module--reviews-text--1z047']")))


    duration  = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='course-card-details-module--row--3sv2A']")))

    org = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='course-card-instructors-module--instructor-list--37tO6']")))
    
    names = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//h3[@data-purpose='course-title-url']")))

    for cur in ratings:

        
        rating.append(cur.text)

    for rev in review:
        reviews.append(rev.text)


    for dur in duration:
        total_duration.append(dur.text)

    for o in org:
        offered_by.append(o.text)

    for n in names:

        name.append(n.text)
    

    


    pass

def automate_udemy(base_url, suffix ,  name, rating, reviews , total_duration,offered_by):

    total_pages = 50

    for i in range(1, total_pages + 1):

        url = base_url + str(i) + suffix

        get_courses(url,  name, rating, reviews , total_duration,offered_by)




import csv


def make_csv(file_name, headers, *lists):
    csv_filename = file_name + ".csv"

    transposed_lists = list(zip(*lists))

    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(headers)

        for row in transposed_lists:
            writer.writerow(row)

    print(f"CSV file '{csv_filename}' has been created.")


if __name__ == '__main__':

    base_url = 'https://www.udemy.com/courses/search/?p='
    suffix = '&q=data+science&src=ukw'

    name = []
    rating = []
    reviews = []
    total_duration = []
    offered_by = []
    automate_udemy(base_url, suffix ,  name, rating, reviews , total_duration,offered_by)

    headers = ["Course Name", "Rating", "Reviews" , "Total Duration" , "Organisation" ] 

    make_csv("Udemy", headers, name, rating, reviews , total_duration,offered_by )

    while True:
        pass
