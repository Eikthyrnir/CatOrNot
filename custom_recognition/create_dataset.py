import requests
import time
import os.path

for i in range(2500):
    cats = "https://thiscatdoesnotexist.com/"
    notCats = "https://picsum.photos/512"

    response = requests.get(cats)
    response.raise_for_status()
    filename = str(i) + ".jpeg"
    completeName = os.path.join("Cat", filename)
    with open(completeName, 'wb') as file:
        file.write(response.content)

    response = requests.get(notCats)
    response.raise_for_status()
    filename = str(i) + ".jpeg"
    completeName = os.path.join("notCat", filename)
    with open(completeName, 'wb') as file:
        file.write(response.content)

    time.sleep(1)
