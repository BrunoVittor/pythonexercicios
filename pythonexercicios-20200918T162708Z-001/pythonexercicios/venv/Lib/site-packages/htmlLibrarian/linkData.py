import datetime
import time

class LinkData(object):

    def __init__(self, alink, html):
        self.link = alink
        self.epochTimeScraped = time.time()
        self.utcTimeScraped = datetime.datetime.utcnow()
        self.html = html

    def __str__(self):
        return '<LinkData object corresponding to '+self.link+' scraped at '+str(self.utcTimeScraped)+'>'

    def get_html(self):
        return self.html
