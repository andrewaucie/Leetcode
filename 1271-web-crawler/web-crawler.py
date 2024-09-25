# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        # BFS on current URL, add if hostname matches
        def getHost(url):
            # take out http://
            return url.split('/')[2]
        host = getHost(startUrl)
        crawled = set([startUrl])
        queue = deque([startUrl])
        while queue:
            currUrl = queue.popleft()
            for nextUrl in htmlParser.getUrls(currUrl):
                if nextUrl not in crawled and getHost(nextUrl) == host:
                    crawled.add(nextUrl)
                    queue.append(nextUrl)
        return crawled