import json
from bs4 import BeautifulSoup as bs
import requests

class InvalidIndex(Exception):
    pass

def get_webpage_data(question_id):
    webpage = 'https://willyoupressthebutton.com/{0}/stats'.format(question_id)
    request = requests.get(
        webpage, 
        headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
        }
    )
    
    soup = bs(request.text, 'html.parser')
    
    main_container = soup.find(id='maincontainer')
    
    if main_container is None:
        raise InvalidIndex({
            "message":"No question found with that index", 
            "index": question_id
        })
    
    stats = [stat for stat in [a for a in main_container.find(id='statsBar').children][1].children]
    
    did_press = stats[1].getText()
    did_press_count = int(did_press.split()[0])
    
    didnt_press = stats[3].getText()
    didnt_press_count = int(didnt_press.split()[0])

    dilemma = [a for a in main_container.find(id='dilemma').children]
    pro = dilemma[1].getText().strip()
    con = dilemma[5].getText().strip()
    
    return {
        'link': webpage,
        'index': question_id,
        'pro': pro,
        'con': con,
        'did_press_count': did_press_count,
        'didnt_press_count': didnt_press_count
    }
    
def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    print("Received context: ",  context)
    for index in range(10000, 10010):
        print(get_webpage_data(index))
    # return event['key1']  # Echo back the first key value
