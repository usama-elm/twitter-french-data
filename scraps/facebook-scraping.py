import os
import time

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# repertoire de resultats
os.chdir(r"C:/Users/HaroldK/PycharmProjects/Inlearning/scraper/results")

# listes pour conserver les resultats
noms = []
textos = []
time_list = []
Comments = []
# imgs = []
# image_src = []
Cnames = []
Ccontents = []
Cdates = []

# Initialisons selenium
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)

options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--mute-audio")
options.add_argument("--start-maximized")
driver = webdriver.Chrome('C:/Users/HaroldK/PycharmProjects/Inlearning/chromedriver.exe', options=options)
driver.get("https://web.facebook.com/")
time.sleep(5)

# target the policy button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[title='Uniquement autoriser les cookies essentiels']"))).click()

# target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

# enter username and password
username.clear()
username.send_keys("Gharden49")
password.clear()
password.send_keys("merrychristmass")

# target the login button and click it

login = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

time.sleep(5)

# We are logged in!

time.sleep(10)

# post research

# driver.get(
#     "https://www.facebook.com/search/posts?q=les%20lions")  # on fait une recherche de publications sur les bots ruses
# time.sleep(4)

link = ["https://www.facebook.com/search/posts?q=vaccins", "https://www.facebook.com/search/posts?q=les%20vaccins", "https://www.facebook.com/search/posts?q=fake%20news","https://www.facebook.com/search/posts?q=ukraine","https://www.facebook.com/search/posts?q=russie","https://www.facebook.com/search/posts?q=guerre%20en%20ukraine","https://www.facebook.com/search/posts?q=invasion%20russe"]
i = 0

while True:
    driver.get(link[i])
    time.sleep(6)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    all_posts = soup.find_all("div", {"class": "du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"})  # pour les posts
    posts = driver.find_element(By.XPATH, "//div[@role='article' and @aria-posinset='1']")  # pour les posts
    for post in all_posts:
        try:
            name = post.find("a", {
                "class": "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gpro0wi8 oo9gr5id lrazzd5p"}).get_text()

        except:
            name = "not found"
        print(name)
        try:
            content = post.find("div", {
                "class": "kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q"}).get_text()
        # except: renvoie une erreur dans le cas il ne retrouve pas l'élément
        except:
            content = "not found"
        print(content)

        # try:
        #     image_src = post.find("img", {
        #         "referrerpolicy": "origin-when-cross-origin"}).get(
        #         "src")
        # # except: renvoie une erreur dans le cas il ne retrouve pas l'élément
        # except:
        #     image_src = "not found"
        # print(image_src)

        try:
            Time = post.find("a", {
                "class": "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw"}).get(
                "aria-label")
            print(Time)
        except:
            Time = "not found"

        try:
            Comment = post.find("span", {
                "class": "d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v b1v8xokw m9osqain"}).get_text()
            print(Comment)
        except:
            Comment = "not found"

        textos.append(content)
        time_list.append(Time)
        noms.append(name)
        Comments.append(Comment)
        #    imgs.append(image_src)
        df = pd.DataFrame({"name": noms, "content": textos, "time": time_list, "comments": Comments})
        df.drop_duplicates(subset="content", keep="first", inplace=True)
        df.to_csv("facebookposts.csv",
                  encoding='utf-8')  # le nom du fichier csv dans lequel on stocke les entêtes de commentaires

        # on clique sur les commentaires pour y avoir accès
        # on clique sur les commentaires pour y avoir accès
        try:
            driver.find_element(By.XPATH, "//span[contains(text(), 'commentaires')]").click()
            time.sleep(3)
        except:
            break

        ViewMore = posts.find_elements(By.XPATH, ".//*[contains(text(), 'plus de commentaires')]")
        time.sleep(3)
        for node in ViewMore:
            try:
                node.click()
                time.sleep(1)
            except:
                pass

        Replies = posts.find_elements(By.XPATH,
                                      ".//*[contains(text(), 'réponse')] | .//*[contains(text(), 'réponses')]")
        for node in Replies:
            try:
                node.click()
                time.sleep(1)
            except:
                pass

        SeeMore = posts.find_elements(By.XPATH, ".//*[contains(text(), 'autres commentaires')]")
        time.sleep(3)
        for node in SeeMore:
            try:
                node.click()
                time.sleep(1)
            except:
                pass

        all_comments = driver.find_elements(By.XPATH,
                                            "//div[@aria-posinset]//div[contains(@aria-label,'Commentaire de') or contains(@aria-label,'Réponse de') ]")

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

            Cnames.append(commentedBy)
            Ccontents.append(commentDescription)

            dfc = pd.DataFrame({"name": Cnames, "comments": Ccontents})
            dfc.drop_duplicates(subset="comments", keep="first", inplace=True)
            dfc.to_csv("facebookcomments" + str(i) +".csv",
                       encoding='utf-8')  # le nom du fichier csv dans lequel on stocke les entêtes de commentaires

            time.sleep(5)
            y = 200
            for timer in range(0, 20):
                driver.execute_script("window.scrollTo(0, " + str(y) + ")")
                y += 200
                time.sleep(1)

        # if df.shape[0] > 1:  # par défaut on se limite à 1 posts, si on veut plus d'infos sur le commentaire on peut changer au niveau
        #     break

    i = i + 1 ### on passe au lien suivant

    if i >= len(link):
        break

driver.quit()
