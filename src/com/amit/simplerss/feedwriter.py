'''
Created on 2 Mar. 2018

@author: Amit.Kumar1
'''
from datetime import datetime
import xml.etree.cElementTree as ET
from com.amit.simplerss.rss_feed import Feed, FeedMessage

#RSS Feed writer:
class RSSFeedWriter:
    def __init__(self, feed, out_file):
        self.feed = feed
        self.out_file = out_file
    
    def write_feed(self):
        root = ET.Element("rss")
        root.attrib = {'version' : '2.0'}
        doc = ET.SubElement(root, 'channel')
        ET.SubElement(doc, 'title').text = self.feed.title
        ET.SubElement(doc, 'link').text = self.feed.link
        ET.SubElement(doc, 'description').text = self.feed.description
        ET.SubElement(doc, 'language').text = self.feed.language
        ET.SubElement(doc, 'published_on').text = self.feed.published_on
        for an_entry in self.feed.entries:
            item = ET.SubElement(doc, 'item')
            ET.SubElement(item, 'title').text = an_entry.title
            ET.SubElement(item, 'link').text = an_entry.link
            ET.SubElement(item, 'description').text = an_entry.description
            ET.SubElement(item, 'author').text = an_entry.author
            ET.SubElement(item, 'guid').text = an_entry.guid
        tree = ET.ElementTree(root)
        tree.write(self.out_file, 'utf-8')

### A feed write example 
title = 'Java 8 Feeds'
feed_link = 'http://localhost:8080/java'
description = 'All Java related stuff from Amit'
language = 'en-US'
published_on = datetime.now().isoformat(timespec='minutes')
rssFeed = Feed(title, feed_link, description, language, published_on)
message_link = 'http://localhost:8080/java/8/streams/streams.rss'
feedMessage = FeedMessage('Java 8 Feeds', message_link, 'An Introduction to Java 8 Streams', 'Amit Kumar', message_link)
rssFeed.entries.append(feedMessage)

feed_writer = RSSFeedWriter(rssFeed, 'c:/Users/Amit.Kumar1/java/8/streams/java8streams.rss')
feed_writer.write_feed()
