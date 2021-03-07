from bs4 import BeautifulSoup
import requests
import json
import os

board_feed_resource_api = 'https://in.pinterest.com/resource/BoardFeedResource/get/?source_url='

board_link = input('Welcome to binterest!\nPaste the link to your board: ')

urls = []

board_url = '/'+board_link.split('/', 3)[-1]

board_html = requests.get(board_link).text
soup = BeautifulSoup(board_html, 'html.parser')
board_id = json.loads(str(soup.find(id='initial-state').string))['resourceResponses'][1]['response']['data'][0]['board']['id']

api_endpoint_data = {
    'options': {
        'bookmarks': [''],
        'isPrefetch': False,
        'board_id':board_id,
        'board_url':board_url,
        'currentFilter':-1,
        'field_set_key':'react_grid_pin_with_board_activity',
        'filter_section_pins': True,
        'sort':'default',
        'layout':'default',
        'page_size':250,
        'redux_normalize_feed': True,
        'no_fetch_context_on_resource': False
    },
    'context': {}
}

while True:
    board_data = requests.get(board_feed_resource_api + board_url + '&data=' + json.dumps(api_endpoint_data)).json()
    pins = board_data['resource_response']['data']
    for pin in pins:
        try:
            urls.append(pin['images']['orig']['url'])
        except KeyError:
            continue
    if board_data['resource']['options']['bookmarks'][0] != '-end-':
        api_endpoint_data['options']['bookmarks'][0] = board_data['resource']['options']['bookmarks'][0]
    else:
        break

if not os.path.exists(os.getcwd().replace('\\','/')+'/boards/'+pins[0]['board']['url']):
    os.makedirs(os.getcwd().replace('\\','/')+'/boards/'+pins[0]['board']['url'])

n=0
for url in urls:
    n=n+1
    r = requests.get(url)
    if not os.path.exists(os.getcwd().replace('\\','/')+'/boards/'+pins[0]['board']['url']+url.split('/')[-1]):
        with open(os.getcwd().replace('\\','/')+'/boards/'+pins[0]['board']['url']+url.split('/')[-1], "wb") as f:
            f.write(r.content)
            print(url.split('/')[-1] + ' downloaded. ' + '[' + str(n) + '/' + str(len(urls)) + ']')
    else:
        print(url.split('/')[-1] + ' retrieved. ' + '[' + str(n) + '/' + str(len(urls)) + ']')