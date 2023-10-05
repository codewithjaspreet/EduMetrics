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



def get_courses(url ,  name, rating, reviews , total_duration,total_enrolled):

    driver.get(url)


    wait = WebDriverWait(driver, timeout= 15)

    ratings = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='course-ratings-label']")))

    review = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='rating-count-label']")))

    enroll = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//b//span")))

    duration  = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='course-info']")))
    names = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//h2[@class='course-name']")))

    for cur in ratings:
        rating.append(cur.text)

    for rev in review:
        reviews.append(rev.text)

    for en in enroll:
        total_enrolled.append(en.text)

    for dur in duration:
        total_duration.append(dur.text)

    for n in names:

        name.append(n.text)
    

    


    pass

def automate_udemy(base_url, suffix ,  name, rating, reviews , total_duration,total_enrolled):

    total_pages = 9

    for i in range(1, total_pages + 1):

        url = base_url + str(i) + suffix

        get_courses(url,  name, rating, reviews , total_duration,total_enrolled)




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

    base_url = 'https://www.mygreatlearning.com/data-science/free-courses?p='
    suffix = '#subject-courses-section'

    name = []
    rating = []
    reviews = []
    total_duration = []
    total_enrolled = []
    automate_udemy(base_url, suffix ,  name, rating, reviews , total_duration,total_enrolled)

    headers = ["Course Name", "Rating", "Reviews" , "Total Duration" , "Total Enrolled" ] 

    make_csv("great_learning", headers, name, rating, reviews , total_duration,total_enrolled )

    while True:
        pass
