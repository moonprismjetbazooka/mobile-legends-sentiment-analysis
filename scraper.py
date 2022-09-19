import os
import pandas as pd
from google_play_scraper import Sort, reviews

# look at https://pypi.org/project/google-play-scraper/ for documentation of google play scraper

def Scraper():
    
    print('Scraping reviews from Google Play Store...')
    results = reviews(
        'com.mobile.legends',
        lang='id',
        country='id',
        count=60000,
        sort=Sort.MOST_RELEVANT
    )

    review_df = pd.DataFrame(results[0]) # results is actually a list with length 2 (first element is the dict containing the reviews)

    data_folder_path = os.path.join(os.getcwd(),'data')

    if not os.path.exists(data_folder_path):
        print('Creating Directory...')
        os.makedirs(data_folder_path)

    print('Writing CSV File...')
    review_df.to_csv(data_folder_path+'\\mobile_legends_reviews.csv')
