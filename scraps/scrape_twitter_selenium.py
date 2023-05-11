from Scweet.scweet import scrape
from Scweet.user import get_user_information, get_users_following, get_users_followers

keywords=["vaccins","ukraine","elections","zemmour","macron"]
results=[]


vac=scrape(hashtag=keywords[0], since="2022-01-01", until="2022-01-03", from_account = None, interval=1, 
                      headless=False, display_type="Top", save_images=False, 
                      lang= "fr",resume=False, filter_replies=False, proximity=False)

vac.to_csv("vaccins.csv")

# scrape(hashtag=keywords[1], since="2022-02-14", until="2022-04-02", from_account = None, interval=1, 
#                       headless=False, display_type="Top", save_images=False, 
#                       lang= "fr",resume=False, filter_replies=False, proximity=False)

# vac.to_csv("ukraine.csv")

# elections=scrape(hashtag=keywords[2], since="2022-01-01", until="2022-04-02", from_account = None, interval=1, 
#                       headless=False, display_type="Top", save_images=False, 
#                       lang= "fr",resume=False, filter_replies=False, proximity=False)

# elections.to_csv("elections.csv")

# zemmour=scrape(hashtag=keywords[3], since="2022-01-01", until="2022-04-02", from_account = None, interval=1, 
#                       headless=False, display_type="Top", save_images=False, 
#                       lang= "fr",resume=False, filter_replies=False, proximity=False)

# zemmour.to_csv("zemmour.csv")

# macron=scrape(hashtag=keywords[4], since="2022-01-01", until="2022-04-02", from_account = None, interval=1, 
#                       headless=False, display_type="Top", save_images=False, 
#                       lang= "fr",resume=False, filter_replies=False, proximity=False)

# macron.to_csv("macron.csv")