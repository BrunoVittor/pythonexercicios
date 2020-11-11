import pickle as pkl
import os
import time
import urllib
from urllib.request import urlopen

try:
	from linkData import LinkData
except ImportError:
	from .linkData import LinkData

class Librarian:
    def __init__(self, rateLimitVal=2, debug=False):
        self.rateLimitVal = rateLimitVal
        self.debug = debug
        self.print('debug mode enabled')

        if not os.path.isdir('librarianTools'):
            self.print('creating librarianTools dir...')
            os.mkdir('librarianTools')

        if not os.path.isdir('htmlLibrary'):
            self.print('creating htmlLibrary dir...')
            os.mkdir('htmlLibrary')

        try:
            self.linkMap = pkl.load(open('./librarianTools/linkMap.pkl', 'rb'))
        except:
            self.linkMap = {}


    def rateLimit(self):
        try:
            lastTime = pkl.load(open('./librarianTools/lastTime.pkl', 'rb'))
        except:
            lastTime = 0
        currentTime = time.time()
        timeToWait = self.rateLimitVal - (currentTime - lastTime)
        if timeToWait > 0:
            self.print('sleeping', timeToWait, 'seconds...')
            time.sleep(timeToWait)
        pkl.dump(time.time(), open('./librarianTools/lastTime.pkl', 'wb'))

    def get_all(self, link):
        if link in self.linkMap:
            mapval = self.linkMap[link]
        else:
            self.linkMap[link] = len(self.linkMap.keys())
            mapval = self.linkMap[link]

        pkl.dump(self.linkMap, open('./librarianTools/linkMap.pkl', 'wb'))
        fileName = './htmlLibrary/html_'+str(mapval)

        try:
            linkDataList = pkl.load(open(fileName, 'rb'))
            assert isinstance(linkDataList, list)
            self.print('found file; loading and returning right now...')
            return linkDataList

        except FileNotFoundError:
            return self.fetch(link, fileName)

    def get(self, link):
        return self.get_all(link)[-1]

    def fetch(self, link, fileName):
        self.print('could not find html for that link in the html store; fetching...')
        self.rateLimit()

        try:
            res = urlopen(link)
            html = res.read()
            self.print('fetched site html!')
            linkData = LinkData(link, html)

            try:
                linkDataList = pkl.load(open(fileName, 'rb'))
            except FileNotFoundError:
                linkDataList = []
            linkDataList.append(linkData)

            pkl.dump(linkDataList, open(fileName, 'wb'))
            return linkDataList

        except urllib.error.HTTPError as e:
            self.print('ran into an HTTPError scraping the site...')
            self.print('HTTPError: ', e.code)
            self.print('setting this site to empty bytes...')
            html = bytes('', 'utf-8')

            if e.code == '404':
                return [LinkData(link, html)]

            linkData = [LinkData(link, html)]
            pkl.dump(linkData, open(fileName, 'wb'))
            return linkData


    def remove(self, link):
        if link in self.linkMap:
            fileName = './htmlLibrary/html_'+str(self.linkMap[link])
            del self.linkMap[link]
            os.remove(fileName)
            self.print('removed', link, 'from my library!')
            return True

        self.print("couldn't find that link in my library!")
        return False


    def setRateLimitVal(rateLimitVal):
        self.rateLimitVal = rateLimitVal

    def print(self, *msg):
        if self.debug:
            print(' '.join([str(s) for s in msg]))
