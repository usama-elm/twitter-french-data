import os
import time
import csv

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# result's directory
os.chdir(r"//directory//")

# selenium Initialization
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--mute-audio")
options.add_argument("--start-maximized")

#driver chrome selection
driver = webdriver.Chrome('C:/Users/HaroldK/PycharmProjects/Inlearning/chromedriver.exe', options=options)
driver.get("https://web.facebook.com/")
time.sleep(5)

# target the policy button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[title='Uniquement autoriser les cookies essentiels']"))).click()

# target username and password
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

# enter username and password
username.clear()
username.send_keys("user")
password.clear()
password.send_keys("password")

# target the login button and click it
login = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

# We are logged in!
time.sleep(10)


# post research ***just post... we will change the line if we search something else
driver.get(
    "https://www.facebook.com/search/posts?q=les%20lions")  #we are doing a research on "les lions"
time.sleep(8)

count = 0
while True:

    soup = BeautifulSoup(driver.page_source, "html.parser")
    all_posts = soup.find_all("div", {"class": "du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"})

    for i in all_posts:

        count += 1
        post = driver.find_element(By.XPATH, "//div[@role='article' and @aria-posinset='1']")  # for the posts
        auth = post.find_element(By.TAG_NAME, 'h3')  # for the authers
        fileName = 'Post' + str(count) + '.csv'
        with open(fileName, 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)  # whe are creating a csv file
            writer.writerow(["Author", "Description"])
            author = auth.text
            description = ''
            try:
                description = post.find_element(By.XPATH,
                                                ".//div[@data-ad-preview='message']//span | .//blockquote//div[@dir='auto']").text
            except:
                description = 'nothing'

            try:
                Date = post.find_element(By.XPATH,
                                                ".//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw']").get_attribute("aria-label")

            except:
                Date = 'nothing'
            print(Date)

            try:
                Comments_number = post.find_element(By.XPATH,
                                                ".//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v b1v8xokw m9osqain']").text
            except:
                Comments_number = 'nothing'
            print(Comments_number)

            writer.writerow([author, description, Date, Comments_number])
            writer.writerow([" ", " "])

            # click on the comments button to acces
            try:
                driver.find_element(By.XPATH, "//span[contains(text(), 'commentaires')]").click()
                time.sleep(5)
            except:
                break

            # click on view more comments to see  more comments
            ViewMore = post.find_elements(By.XPATH, ".//*[contains(text(), 'Voir plus de commentaires')]")
            time.sleep(5)
            for node in ViewMore:
                try:
                    node.click()
                    time.sleep(1)
                except:
                    pass

            # click on answers to see answers
            Replies = post.find_elements(By.XPATH, ".//*[contains(text(), 'réponse')] | .//*[contains(text(), 'réponses')]")
            for node in Replies:
                try:
                    node.click()
                    time.sleep(1)
                except:
                    pass
            # to see more
            SeeMore = post.find_elements(By.XPATH, ".//*[contains(text(), 'autres commentaires')]")
            time.sleep(5)
            for node in SeeMore:
                try:
                    node.click()
                    time.sleep(1)
                except:
                    pass

            # count all the comments
            all_comments = driver.find_elements(By.XPATH,
                                                "//div[@data-visualcompletion='ignore-dynamic']/div/div/ul/li//div[@role='article' and @tabindex='-1']")


            # scrap the available comments
            for comment in all_comments:
                commentedBy = comment.find_element(By.XPATH, ".//span/span[@dir='auto']").text
                commentDescription = ''

                print(commentedBy)

                try:
                    commentDescription = comment.find_element(By.XPATH,
                                                           ".//div[@dir='auto']").text
                except:
                    commentDescription = ''
                print(commentDescription)
                writer.writerow([commentedBy, commentDescription])
                writer.writerow([' ', ' '])

    #to scrol down
    time.sleep(5)
    y = 500
    for timer in range(0, 25):
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 500
        time.sleep(3)

    driver.quit()