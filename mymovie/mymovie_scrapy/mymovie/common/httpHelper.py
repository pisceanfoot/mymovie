from urlparse import urlparse
from urlparse import urljoin


def getUrl(main, url):
    if(not url):
        raise Exception('url can not be null or empty')

    tmpUrl = url.lower()
    if(tmpUrl.startswith('http://') or tmpUrl.startswith('https://')):
        return url

    if(url.startswith('?')):
        index = main.find('?')
        if index != -1:
            newUrl = main[0: index]
        else:
            newUrl = main

        newUrl += url
    else:
        newUrl = urljoin(main, url)

    newUrl = newUrl.replace('&amp;', '&')
    return newUrl


if __name__ == '__main__':
    
    url = getUrl('http://test', 'http://www.newurl.com')
    print url

    url = getUrl('http://test/', '?id=7')
    print url

    url = getUrl('http://test/?name=8', '?id=7')
    print url

    url = getUrl('http://test/a.html?name=8', '?id=7')
    print url

    url = getUrl('http://test/a.html?name=8', 'b.html')
    print url

    url = getUrl('http://test/a.html?name=8', '/b.html?id=9')
    print url

    url = getUrl('http://test/folder/a.html?name=8', 'b.html')
    print url

    url = getUrl('http://test/folder/a.html?name=8', '/b.html?id=10')
    print url