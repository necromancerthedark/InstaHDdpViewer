from instagram_private_api import Client, ClientCompatPatch
from PIL import Image
import requests
from io import BytesIO
import getpass
import json

secret = open("secret.json", "r")
details = json.loads(secret.read())
api = Client(details['username'], details['password'])
results = api.feed_timeline()

names = open('people.txt', 'r')
target_user_id = names.readline().strip()
while target_user_id != "":
    file_name = target_user_id + '.jpg'
    details = api.user_detail_info(target_user_id)
    imdataurl = details['user_detail']['user']['hd_profile_pic_url_info']['url']
    image = requests.get(imdataurl)
    img = Image.open(BytesIO(image.content))
    img.save(file_name)
    target_user_id = names.readline().strip()
