import os.path
import requests
from pathlib import Path


def save_from_url_to_dir(url: str, file_name: str):
    response = requests.get(url)
    response.raise_for_status()
    with open(file_name, 'wb') as file:
        file.write(response.content)


# categories and corresponding urls to download images
category_urls = {
    "cat_images":       "https://thiscatdoesnotexist.com/",
    "horse_images":     "https://thishorsedoesnotexist.com/",
    "art_images":       "https://thisartworkdoesnotexist.com/"
}

# create directories of not exists
for category in category_urls.keys():
    Path(category).mkdir(parents=True, exist_ok=True)

# number of images for every category to download
dataset_size = 100
for i in range(dataset_size):
    filename = str(i) + ".jpeg"
    for category, url in category_urls.items():
        save_from_url_to_dir(url, os.path.join(category, filename))
