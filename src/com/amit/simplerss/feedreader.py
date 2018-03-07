'''
Created on 5 Mar. 2018

@author: Amit.Kumar1
'''

import urllib.request 
import urllib.error
from xml.etree.ElementTree import XMLPullParser, ParseError
from com.amit.simplerss.rss_feed import FeedMessage, Feed

# RSS Feed reader
class RSSFeedReader:
    
    def __init__(self, url):
        self.url = urllib.request.Request(url)
    
    def read(self):
        try:
            resource = urllib.request.urlopen(self.url)
            data = resource.read().decode('utf-8')
        except urllib.error.HTTPError as httpex:
            print('The Server could not fulfill the request')
            print('Error code: ', httpex.code)
        except urllib.error.URLError as urlex:
            print('Failed to reach the server.')
            print(urlex.all_reasons())
        else:
            return data
    
    
    def read_feed(self):
        feed = None
        is_feed_header = True
        description = ''
        title = ''
        link = ''
        language = ''
        author = ''
        published_on = ''
        guid = ''
        try:
            data = self.read()
            parser = XMLPullParser(['start', 'end'])
            parser.feed(data)
            for event, elem in list(parser.read_events()):
                if event == 'start':
                    local_part = elem.tag
                    if local_part == 'item':
                        if is_feed_header == True:
                            is_feed_header = False
                            feed = Feed(title, link, description, language, published_on)
                        
                    elif local_part == 'title':
                        title = elem.text
                    elif local_part == 'description':
                        description = elem.text
                    elif local_part == 'link':
                        link = elem.text
                    elif local_part == 'guid':
                        guid =elem.text
                    elif local_part == 'language':
                        language = elem.text
                    elif local_part == 'author':
                        author = elem.text
                    elif local_part == 'published_on':
                        published_on = elem.text
                    elif event == 'end':
                        if elem.get_tag() == 'item':
                            feed_message = FeedMessage(title, link, description, author, guid)
                            feed.entries.append(feed_message)
                            continue
        except ParseError as pe:
            print(str(pe.code) + ": " + pe.get_reason())
        
        return feed

### A feed read example
a_feed_reader = RSSFeedReader("http://localhost:8080/java/8/streams/streams.rss")
feed = a_feed_reader.read_feed()
print(feed)
for an_entry in feed.entries:
    print(an_entry)
