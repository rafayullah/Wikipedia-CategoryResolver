import requests
import json
import re

class Wiki:

    def __init__(self):
        self.S = requests.Session()
        self.URL = "https://en.wikipedia.org/w/api.php"

    def get_page_name(self,SEARCHPAGE):
        PARAMS = {
            'action':"query",
            'list':"search",
            'srsearch': SEARCHPAGE,
            'format':"json"}

        R = self.S.get(url=self.URL, params=PARAMS)
        DATA = R.json()
        pages = ''
        
        try:
            if SEARCHPAGE.lower() in DATA['query']['search'][0]['title'].lower():
                snippet = DATA['query']['search'][0]['snippet']
                snippet = re.sub(r'<.*?>', '', snippet)
                page = DATA['query']['search'][0]['title']
                return page,snippet
            else:
                print('No results found')
                return None,None
        except:
            print('No results found')
            return None,None

    def get_category(self,query):

        page,snippet = self.get_page_name(query)

        if page == None:
            return None

        PARAMS = {
            'action': "parse",
            'page': page,
            'format': "json"}

        R = self.S.get(url=self.URL, params=PARAMS)
        data = R.json()

        category = []
        extras = ['page','article']
        categories = data['parse']['categories']
        for i in categories:
            text = i['*'].lower().strip()
            if ('page' not in text) & ('article' not in text) & ('date' not in text) & ('all' not in text) & ('redirect' not in text) & ('wiki' not in text) & ('webarchive' not in text) & ('cs1' not in text) & ('use_american_english' not in text) & ('template' not in text):
                category.append(text)

        return {'topic':page, 'snippet':snippet,'categories':category}