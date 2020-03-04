
''' Tools to use when scraping
'''
import os

# Generalize this
# def cached(scraper, cache_path, *scraper_args):
#     """ Cache a scraper
#     """
#     if not os.path.exists(cache_path):
#         data = func(*scraper_args)
#         data.to_csv(path, index = False)
#         print("Scraped from web.")
#     else:
#         data = pd.read_csv(path)
#         print("Read from file.")
#     return data