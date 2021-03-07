import requests
import os

board_feed_resource = input('Paste the link you got from your console: ')

pins = requests.get(board_feed_resource).json()['resource_response']['data']

urls = []

for pin in pins:
    try:
        url = pin['images']['orig']['url']
        urls.append(url)
    except KeyError:
        break

if not os.path.exists(os.getcwd().replace('\\','/')+'/boards/'+pins[0]['board']['url']):
    os.makedirs(os.getcwd().replace('\\','/')+'/boards/'+pins[0]['board']['url'])

for url in urls:
    r = requests.get(url)
    with open(os.getcwd().replace('\\','/')+'/boards/'+pins[0]['board']['url']+url.split('/')[-1], "wb") as f:
        f.write(r.content)