'''
Created on 13 Mar. 2018

@author: Amit.Kumar1
'''
from collections import deque
import requests
from bs4 import BeautifulSoup
import re

def is_relative_path(a_path):
    match_obj = re.search("^/\w", a_path)
    return match_obj is not None
    
def get_content_type(http_resp):
    content_type = http_resp.headers['content-type']
    
    if content_type.startswith("application/json"):
        cont_type = 'json'
    elif content_type.startswith("text/html"):
        cont_type = 'html'
    else:
        cont_type = ''
    return cont_type


def process_http_response(http_resp, url, visited_sites):
    # check response status
    if http_resp.status_code == 200:
        # get the HTTP content-type
        cont_type = get_content_type(http_resp)
        if cont_type == 'html':
            # parse the html to get all the links
            links = set()
            soup = BeautifulSoup(http_resp.text, "lxml")
            for alink in soup.find_all('a'):
                if alink.has_attr('href'):
                    link_url = alink.get('href')
                    if is_relative_path(link_url):
                        link_url = url + link_url
                    elif link_url.startswith('//'):
                        link_url = "http:" + link_url
                    else: #link_url.startswith('#') or len(link_url.strip()) == 0:
                        continue
                    links.add(link_url)
                    #print(alink['href'])
            visited_sites[url] = links
    else:
        # Something went wrong
        pass
'''
'''
initial_site = 'https://www.slashdot.org'
unvisited_queue = deque()
unvisited_queue.append(initial_site)
visited_sites = {}
visited_count = 0
while visited_count < 50:
    try:
        a_link = unvisited_queue.popleft()
    except IndexError as ie:
        print(ie.all_reasons())
        break
    if a_link not in visited_sites:
        http_resp = requests.get(a_link, stream=True, timeout=20)
        visited_count += 1
    
        # Need to process the response here
        process_http_response(http_resp, a_link, visited_sites)
        
        # Now put the new unvisited links in the unvisited queue
        new_links = visited_sites.get(a_link)
        if new_links is not None:
            for link in new_links:
                if link not in visited_sites:
                    unvisited_queue.append(link)
    else:
        pass

for visited in visited_sites.keys():
    print(visited)
