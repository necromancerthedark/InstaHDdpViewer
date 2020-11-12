from instagram_private_api import Client, ClientCompatPatch
from PIL import Image
import requests
from io import BytesIO
import getpass

username = input("Enter Your Username: ")
password = getpass.getpass('Password: ')
api = Client(username, password)
results = api.feed_timeline()

target_user_id = input('Enter User Id: ')
file_name = target_user_id + '.jpg'
details = api.user_detail_info(target_user_id)
imdataurl = details['user_detail']['user']['hd_profile_pic_url_info']['url']
image = requests.get(imdataurl)
img = Image.open(BytesIO(image.content))
img.show()
img.save(file_name)
